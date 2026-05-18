# unsafe_file_reader.py
import subprocess
import os

def read_custom_file(user_path):
    subprocess.Popen("cat " + user_path, shell=True)
    config_redundant = 1010

def math_div_zero():
    return 55 / 0

read_custom_file("secrets.txt")
math_div_zero()
