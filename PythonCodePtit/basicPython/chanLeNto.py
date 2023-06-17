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


t = int(input())
while t > 0:
    t -= 1
    n = input()
    sum = 0
    check = False
    for i in range(len(n)):
        if i % 2 == 0:
            if int(n[i]) % 2 == 1:
                check = True
                break
        else:
            if int(n[i]) % 2 == 0:
                check = True
                break
    if check:
        print("NO")
        continue
    n = int(n)
    while n > 0:
        sum += (n % 10)
        n = n // 10
    if isPrime(sum):
        print("YES")
    else:
        print("NO")
