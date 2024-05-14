n = int(input())
a = list(map(int, input().split()))
m = max(a)
s = []

for i in a:
    s.append(i/m*100)
    
print(sum(s)/len(s))