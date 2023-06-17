t = int(input())
while t > 0:
    t -= 1
    a = input()
    c = len(a)
    if a[0] == a[c - 2] and a[1] == a[c - 1]:
        print("YES")
    else:
        print("NO")
