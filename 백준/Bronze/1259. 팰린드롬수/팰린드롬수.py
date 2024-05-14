while True:
    a = input()
    
    if int(a) == 0:
        break
    
    for i in range(0, int(len(a)/2)):
        if a[i] == a[len(a)-1-i]:
            continue
        else:
            print("no")
            break
    else:
        print("yes")