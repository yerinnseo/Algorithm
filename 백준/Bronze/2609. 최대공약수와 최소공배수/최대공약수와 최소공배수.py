a, b = map(int, input().split())
l1 = []
l2 = []

for i in range(1, a+1):
    if a%i == 0:
        l1.append(i)

for i in range(1, b+1):
    if b%i == 0:
        l2.append(i)

common_list = list(set(l1) & set(l2))

c = max(common_list)

print(c)
print(int(a*b/c))