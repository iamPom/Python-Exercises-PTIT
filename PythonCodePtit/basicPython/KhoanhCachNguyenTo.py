import math


def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
    return True


n, x = map(int, input().split())
arrPrime = [2, 3]
index = 3
while len(arrPrime) <= n:
    index += 2
    if isPrime(index):
        arrPrime.append(index)

for i in range(n + 1):
    print(x, end=" ")
    x += arrPrime[i]
