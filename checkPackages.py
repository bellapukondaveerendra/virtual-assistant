import subprocess
import sys
import os

output = subprocess.check_output(["where", "notepad.exe"])
print(output.decode("utf-8"))

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
print(installed_packages)