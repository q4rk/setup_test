# untrusted_code.py
import os
import sys

def run_user_command(user_input):
    # CRITICAL: Security command injection vulnerability
    os.system("echo " + user_input)

if __name__ == "__main__":
    run_user_command(sys.argv[1])
