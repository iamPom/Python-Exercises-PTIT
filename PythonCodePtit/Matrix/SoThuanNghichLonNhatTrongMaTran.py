import sys


def isThuanNghich(x):
    s = str(x)
    return s == s[::-1] and x > 10


row, col = map(int, input().split())
a = [[int(j) for j in input().split()] for i in range(row)]
res = a[0][0]
check = True
for i in range(row):
    for j in range(col):
        if a[i][j] > res and isThuanNghich(a[i][j]):
            res = a[i][j]
            check = False
if check:
    print("NOT FOUND")
    sys.exit()
print(res)
for i in range(row):
    for j in range(col):
        if a[i][j] == res:
            print("Vi tri [" + str(i) + "][" + str(j) + "]")
