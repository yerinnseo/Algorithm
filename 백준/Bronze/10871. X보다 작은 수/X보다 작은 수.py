n, x = map(int, input().split())
a = input().split()

for num in a:
    if int(num) < x:
        print(num, end = " ")