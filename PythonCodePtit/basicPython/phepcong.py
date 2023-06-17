s = input()
if s[2] == "+":
    if int(s[0]) + int(s[4]) == int(s[8]):
        print("YES")
    else:
        print("NO")
if s[2] == "-":
    if int(s[0]) - int(s[4]) == int(s[8]):
        print("YES")
    else:
        print("NO")
