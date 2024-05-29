import sys

l = int(input())
s = sys.stdin.readline()
sum = 0

for i in range(0, l):
    sum += (ord(s[i]) - 96) * (31 ** i)
    
print(sum)