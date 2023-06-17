# code:  	PY01020
t = int(input())
while t > 0:
    t -= 1
    a = input()
    ok = True
    for i in range(0, len(a)):
        if a[i] != '4' and a[i] != '7':
            print("NO")
            ok = False
            break
    if ok:
        print("YES")
