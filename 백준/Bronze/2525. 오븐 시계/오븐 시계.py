a, b = map(int, input().split())
c = int(input())

if b + c >= 60:
    if a + ((b + c) // 60) > 23:
        print (str(a + ((b + c) // 60) - 24) + " " + str((b + c) % 60))
    else:
        print (str(a + ((b + c) // 60)) + " " + str((b + c) % 60))    
else:
    print (str(a) + " " + str(b + c))