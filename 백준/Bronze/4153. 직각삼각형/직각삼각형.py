while True:
        a = sorted(list(map(int, input().split())))
        if a[0] == a[1] == a[2] == 0:
            break
        if a[0]**2 + a[1]**2 == a[2]**2:
            print("right")
        else:
            print("wrong")