t = int(input())
while t > 0:
    t -= 1
    a = int(input())
    res = 1
    while a > 0:
        if (a % 10 != 0):
            res *= (a % 10)
        a //= 10
    print(res)

