import sys
import time

time.sleep(2)
a = sys.argv[1]
with open('text.txt', 'w') as f:
    f.write(a)
print(a * 3)
