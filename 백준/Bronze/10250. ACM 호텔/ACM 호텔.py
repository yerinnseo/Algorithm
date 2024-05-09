T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    cnt = 0
    for i in range(1, w+1):
        for j in range(1, h+1):
            cnt += 1
            
            if cnt == n:
                if i > 9:
                    print(str(j)+str(i))
                else:
                    print(str(j)+"0"+str(i))