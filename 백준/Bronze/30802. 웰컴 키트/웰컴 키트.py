import sys, math

n = int(sys.stdin.readline())
tshirts = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())
set = 0

for i in range(0, 6):
    set += math.ceil(tshirts[i]/t)

print(set)
print(int(n/p), n%p)