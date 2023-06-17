import math


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


t = int(input())
while t>0:
    t-=1
    n = input()
    num = n[len(n) - 4:]
    if isPrime(int(num)):
        print("YES")
    else:
        print("NO")
