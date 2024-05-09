t = int(input())

for _ in range(t):
    s = input()
    sum = 0
    score = 0
    
    for i in s:
        if i == "O":
            sum += 1
            score += sum
        else:
            sum = 0
    print(score)