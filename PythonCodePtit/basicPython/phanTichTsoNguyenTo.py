import math

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    print("1", end=' ')
    c1 = 0
    while n % 2 == 0:
        n //= 2
        c1 += 1
    if c1 > 0:
        print("* 2^" + str(c1), end=' ')
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            print("* " + str(i) + "^" + str(count), end=' ')
    if n > 1:
        print("* " + str(n) + "^1", end=' ')
    print()