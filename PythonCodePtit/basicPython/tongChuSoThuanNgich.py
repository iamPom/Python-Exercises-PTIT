def isThuanNghic(x):
    x = str(x)
    if len(x) < 2:
        return False
    return x == x[::-1]


t = int(input())
while t > 0:
    t -= 1
    num = input()
    sumdigit = 0
    for i in num:
        sumdigit += int(i)
    if isThuanNghic(sumdigit):
        print("YES")
    else:
        print("NO")
