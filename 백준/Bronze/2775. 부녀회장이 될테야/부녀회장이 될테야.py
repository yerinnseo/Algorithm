T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    a = []
    for i in range(1, 16):
        a.append(i)
    
    for i in range(0, k):
        for j in range(1, n+1):
            a[j] += a[j-1]
    print(a[j-1])