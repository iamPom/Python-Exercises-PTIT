import math


def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1


n = int(input())
a = [int(i) for i in input().split()]
lst = []
for i in a:
    if isPrime(int(i)):
        lst.append(i)
lst.sort()
index = 0
for i in a:
    if isPrime(i):
        print(lst[index],end=" ")
        index += 1
    else:
        print(i, end=" ")