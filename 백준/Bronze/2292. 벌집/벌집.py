import sys

n = int(sys.stdin.readline())-1
d = 0

while 3*d*(d+1) < n:
    d += 1
    
print(d+1)