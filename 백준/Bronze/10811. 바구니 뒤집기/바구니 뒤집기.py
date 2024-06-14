n, m = map(int, input().split())

a = [i for i in range(0, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    for _ in range((j - i + 1)//2):
        temp = a[j]
        a[j] = a[i]
        a[i] = temp
        j -= 1
        i += 1

print(*a[1:])