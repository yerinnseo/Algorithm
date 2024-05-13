n = int(input())
nums = list(map(int, input().split()))
sum = 0

for i in nums:
    for j in range(2, i+1):
        if i%j == 0:
            if i == j:
                sum += 1
            else:
                break

print(sum)