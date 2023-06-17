def soChuSoChan(x):
    return len(str(x)) % 2 == 0


def chuSoChan(x):
    x = str(x)
    for i in x:
        if int(i) % 2 == 1:
            return False
    return True


def isThuanNghic(x):
    x = str(x)
    return x == x[::-1]


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(22, n, 22):
        if isThuanNghic(i) and soChuSoChan(i) and chuSoChan(i):
            print(i, end=' ')
    print()
