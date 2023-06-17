import math


def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1
n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
    if i not in b:
        b.append(i)
check=True
for i in range(len(b)):
    sum1 = sum(b[0:int(i) + 1])
    sum2 = sum(b[int(i) + 1:])
    if isPrime(sum1) and isPrime(sum2):
        print(i)
        check = False
        break
if check:
    print("NOT FOUND")