import math


# def isPrime(n):
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(math.sqrt(n))+1, 2):
#             if n % i == 0:
#                 return False
#     return True
def isPrime(n):
    if n < 4:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def USCLN_1(a, b):
    if b == 0:
        return a
    return USCLN_1(b, a % b)


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    count = 0
    for i in range(1, n):
        if USCLN_1(n, i) == 1:
            count += 1
    if isPrime(count):
        print("YES")
    else:
        print("NO")
