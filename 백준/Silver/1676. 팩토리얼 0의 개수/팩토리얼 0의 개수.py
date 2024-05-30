n = int(input())
sum = 1

while n > 0:    
    sum *= n
    n -= 1

a = str(sum)
count = 0

for i in range(0, len(a)):
    if a[len(a)-1-i] == '0':
        count += 1
    else:
        print(count)
        break