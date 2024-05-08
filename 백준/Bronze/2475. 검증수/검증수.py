a = list(map(int, input().split()))
a2 = []

for i in range (0, 5):
    a2.append(a[i]*a[i])

print((sum(a2))%10)