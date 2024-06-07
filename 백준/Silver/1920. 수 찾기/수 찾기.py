import sys

n = int(input())
a = set(map(int, sys.stdin.readline().split()))

m = int(input())
mlist = list(map(int, input().split()))

for i in range(0, m):
    if mlist[i] in a:
        print(1)
    else:
        print(0)