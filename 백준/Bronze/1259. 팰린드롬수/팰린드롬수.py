import sys

while True:
    n = sys.stdin.readline()[:-1]
    
    if n == '0':
        break
    
    if n == n[::-1]:
        print("yes")
    else:
        print("no")