N = int(input())
m = 1
if N == 0:
    print(1)
else:
    for i in range(1, N+1):
        m *= i
    print(m)