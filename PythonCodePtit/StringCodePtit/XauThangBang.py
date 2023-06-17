from builtins import input

t = int(input())
while t > 0:
    t -= 1
    s1 = input()
    s1 = list(s1)
    s2 = list(s1)
    list.reverse(s2)
    check = True
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
