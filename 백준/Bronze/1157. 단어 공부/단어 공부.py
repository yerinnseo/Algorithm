import sys

s = sys.stdin.readline().upper()
a = []

for i in range(0, 26):
    a.append(s.count(chr(65+i)))

if a.count(max(a)) > 1:
    print("?")
else:
    print(chr(a.index(max(a))+65))