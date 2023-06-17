t = int(input())
while t > 0:
    t -= 1
    s = input()
    if (len(s) % 2 == 0):
        print("NO")
        continue
    if (s[1] == s[2]):
        print("NO")
        continue
    for i in range(2, len(s), 2):
        if (s[i] != s[i - 2]):
            print("NO")
            continue
    print("YES")
