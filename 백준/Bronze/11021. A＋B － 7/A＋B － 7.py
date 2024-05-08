T = int(input())
num = 0

for i in range(1, T+1):
    a, b = map(int, input().split())
    num += 1
    print("Case #{0}:".format(num), a+b)