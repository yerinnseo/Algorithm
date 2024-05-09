t = int(input())

for i in range(1, t+1):
    r, s = map(str, input().split())
    string = []

    for j in range(0, len(s)):
        string.append(s[j]*int(r))
    print(''.join(string))