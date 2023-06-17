import math

a = [1] * 10001
a[0] = a[1] = 0
for i in range(2, int(math.sqrt(10001))):
    if a[i]:
        for j in range(i * i, 10001, i):
            a[j] = 0


def countMax(n):
    count = 0
    n1 = n2 = n
    while not a[n1] and not a[n2]:
        n1 -= 1
        n2 += 1
        count += 1
    return count


input()
print(max([countMax(int(i)) for i in input().split()]))
