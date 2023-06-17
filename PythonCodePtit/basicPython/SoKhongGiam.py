# code:  	PY01020
t = int(input())
while t > 0:
    t -= 1
    s = str(input())
    ok = 1
    c = len(s)
    for i in range(0, c - 1):
        if s[i] > s[i + 1]:
            print("NO")
            ok = 0
            break
        else:
            continue
    if ok == 1:
        print("YES")
