import math
import sys


def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1


row, col = map(int, input().split())
a = [[int(j) for j in input().split()] for i in range(row)]
res = a[0][0]
check = True
for i in range(row):
    for j in range(col):
        if a[i][j] > res and isPrime(a[i][j]):
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
