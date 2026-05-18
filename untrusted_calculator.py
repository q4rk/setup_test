# untrusted_calculator.py
import subprocess
import os # Style: Unused import

def ping_host(ip_address):
    # CRITICAL SECURITY BUG: Command Injection vulnerability
    subprocess.Popen("ping -c 1 " + ip_address, shell=True)
    
    # Style: Unused variable
    redundant_config = 42

def calculate_quotient():
    # CRITICAL BUG: Division by zero risk
    crash_val = 50 / 0
    return crash_val

ping_host("127.0.0.1")
calculate_quotient()
