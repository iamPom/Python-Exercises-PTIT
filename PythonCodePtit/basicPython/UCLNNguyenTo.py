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


def USCLN_1(a, b):
    if b == 0:
        return a
    return USCLN_1(b, a % b)


# def USCLN(a, b):
#     while a > 0:
#         if a < b:
#             a, b = b, a
#         a %= b
#     return b
t = int(input())
while t > 0:
    t -= 1
    a, b = input().split()
    a, b = int(a), int(b)
    n = USCLN_1(a, b)
    sum = 0
    while n > 0:
        sum += (n % 10)
        n = n // 10
    if isPrime(sum):
        print("YES")
    else:
        print("NO")
