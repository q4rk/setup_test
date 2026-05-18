# Pull Request Review Instructions

You are performing an automated Pull Request review.
The repository is `q4rk/setup_test`.
The Pull Request number is `1`.

When calling GitHub MCP tools (such as `pull_request_read.get`, `pull_request_read.get_diff`, `create_pending_pull_request_review`, `add_comment_to_pending_review`, or `submit_pending_pull_request_review`), you MUST pass these exact literal values:
- `repository`: "q4rk/setup_test"
- `pull_request_number`: 1

Do not use environment variables like `$REPOSITORY` or `$PULL_REQUEST_NUMBER` in your python tool call arguments. Use the literal string "q4rk/setup_test" and the literal number 1.
