n, m = map(int, input().split())

a = [i for i in range(0, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    for k in range(0, (j - i + 1) // 2):
        temp = a[j - k]
        a[j - k] = a[i + k]
        a[i + k] = temp
        
print(*a[1:])