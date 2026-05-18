# vulnerable_network.py
import subprocess
import sys

def check_ping(host):
    subprocess.Popen("ping -c 1 " + host, shell=True)
    redundant_config = 123

def execute_zero_crash():
    return 99 / 0

check_ping("8.8.8.8")
execute_zero_crash()
