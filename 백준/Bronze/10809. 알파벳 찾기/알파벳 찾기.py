s = input()
list = []

for i in range(0, 26):
    if chr(97+i) in s:
        list.append(s.index(chr(97+i)))
    else:
        list.append(-1)
        
print(*list)