import math
from builtins import int


def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True


n = int(input())
list1 = [int(i) for i in input().split()]
list2 = []
for i in list1:
    if i not in list2 and isPrime(i):
        print(i, list1.count(i))
        list2.append(i)
