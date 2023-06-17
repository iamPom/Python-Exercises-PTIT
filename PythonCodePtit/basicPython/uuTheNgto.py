import math


def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1


t = int(input())
for i in range(t):
    num = input()
    if not isPrime(int(len(num))):
        print("NO")
        continue
    countprime = 0
    for i in num:
        if isPrime(int(i)):
            countprime += 1
    if countprime > int(len(num) // 2):
        print("YES")
    else:
        print("NO")
