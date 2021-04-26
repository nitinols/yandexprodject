import subprocess
import sys
from subprocess import Popen

program = "test.py"
process = subprocess.run([sys.executable, program], input=b'23')
process1 = subprocess.run([sys.executable, program], input=b'33')
process2 = subprocess.run([sys.executable, program], input=b'43')
print(3)