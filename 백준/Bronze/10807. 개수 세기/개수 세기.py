N = input()
a = input().split()
v = int(input())
sum = 0

for i in a:
    if int(i) == v:
        sum += 1

print(sum)