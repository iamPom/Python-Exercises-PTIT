def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
    return True


def outputMatrix():
    for i in range(row):
        for j in range(col):
            print(arr2d[i][j], end=" ")
        print()


row, col = input().split()
row, col = int(row), int(col)
arr2d = [[int(j) for j in input().split()] for i in range(row)]
for i in range(row):
    for j in range(col):
        if isPrime(arr2d[i][j]):
            arr2d[i][j] = 1
        else:
            arr2d[i][j] = 0
outputMatrix()
