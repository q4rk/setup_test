#!/bin/bash
set -ex  # Fail immediately on errors and print commands as they run

# 1. Your existing build/test commands (if any)
# e.g., pytest extensive_test.py

# 2. Run your Buganizer sync script!
python3 scripts/update_buganizer.py
