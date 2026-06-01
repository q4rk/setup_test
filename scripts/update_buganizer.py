#!/usr/bin/env python3
"""Louhi custom script to parse commit messages and update Buganizer tickets.

Runs privately inside the secure internal Kokoro network.
"""

import os
import re
import subprocess
import urllib.request
import urllib.error
import json

# 1. Configuration Details
# The API key is required by OnePlatform but is NOT sensitive (not used for authentication).
# You can safely hardcode it or read it from environment variables.
BUGANIZER_API_KEY = os.getenv("BUGANIZER_API_KEY", "YOUR_PUBLIC_ONEPLATFORM_API_KEY_HERE")
BUGANIZER_API_URL = "https://issuetracker.corp.googleapis.com/v1/issues"

# 2. Regex Pattern for matching Buganizer IDs (e.g., BUG: b/123456 or FIXED: b/78910)
BUG_REGEX = re.compile(r"^(?:BUG|Bugs|BUGFIX|FIX|FIXED|FIXING|FIXES):\s*(?:b/)?(\d+)", re.IGNORECASE)

def get_git_commits():
    """Fetches commit messages from the most recent push/merge."""
    try:
        # Reads the commit log from HEAD~1 to HEAD (the last merged commit details)
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%B"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error reading git logs: {e.stderr}")
        return []

def extract_bug_ids(commit_lines):
    """Extracts Buganizer IDs matching the required line-start syntax."""
    bug_ids = []
    for line in commit_lines:
        match = BUG_REGEX.match(line.strip())
        if match:
            bug_ids.append(match.group(1))
    return bug_ids

def get_metadata_oauth_token():
    """Queries the local GCE Metadata Server to fetch the GCP service account access token."""
    metadata_url = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"
    req = urllib.request.Request(metadata_url)
    req.add_header("Metadata-Flavor", "Google")
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            return data.get("access_token")
    except Exception as e:
        print(f"Warning: Failed to fetch OAuth token from GCE Metadata Server: {e}")
        return None

def post_comment_to_buganizer(bug_id, commit_msg):
    """Appends a standard tracking comment to the Buganizer issue."""
    url = f"{BUGANIZER_API_URL}/{bug_id}/comments?key={BUGANIZER_API_KEY}"
    
    # Generate the comment payload
    comment_text = (
        f"🤖 [Louhi Sync] A code change has been merged on GitHub:\n\n"
        f"Commit Details:\n"
        f"-------------------\n"
        f"{commit_msg}\n"
    )
    payload = {
        "comment": comment_text
    }
    
    headers = {
        "Content-Type": "application/json",
    }
    
    # Fetch the GCE service account OAuth token and inject as Bearer auth header
    token = get_metadata_oauth_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    else:
        print("Warning: Proceeding without Authorization header (may fail in secure environments).")

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    try:
        # OAuth/Gaia authentication is handled automatically by the Kokoro environment.
        with urllib.request.urlopen(req) as response:
            print(f"Successfully posted comment to bug b/{bug_id}. Status: {response.status}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error when calling Buganizer API for b/{bug_id}: {e.code} - {e.read().decode()}")
    except Exception as e:
        print(f"Failed to call Buganizer API for b/{bug_id}: {e}")

def main():
    print("Starting Louhi Buganizer Sync Script...")
    commit_lines = get_git_commits()
    if not commit_lines:
        print("No commits detected. Exiting.")
        return
        
    commit_msg = "\n".join(commit_lines)
    bug_ids = extract_bug_ids(commit_lines)
    
    if not bug_ids:
        print("No Buganizer BUG or FIX tags found in commit message. Done.")
        return
        
    print(f"Found Buganizer IDs to update: {bug_ids}")
    for bug_id in bug_ids:
        post_comment_to_buganizer(bug_id, commit_msg)

if __name__ == "__main__":
    main()
