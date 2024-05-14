a = list(map(int, input().split()))
b = []

b.append(1-a[0])
b.append(1-a[1])
b.append(2-a[2])
b.append(2-a[3])
b.append(2-a[4])
b.append(8-a[5])

print(*b)