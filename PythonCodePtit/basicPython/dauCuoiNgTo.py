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
for i in range(t):
    n = input()
    num1 = int(n[:3])
    num2 = int(n[len(n) - 3:])
    if isPrime(num1) and isPrime(num2):
        print("YES")
    else:
        print("NO")
