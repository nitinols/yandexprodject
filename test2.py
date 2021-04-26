import subprocess
import sys

program = "test.py"
process = subprocess.Popen([sys.executable, program, '32'])

