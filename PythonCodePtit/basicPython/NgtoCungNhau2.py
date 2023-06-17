def USCLN_1(a, b):
    if b == 0:
        return a
    return USCLN_1(b, a % b)


n, k = map(int, input().split())
count = 0
for i in range(10 ** (k - 1), 10 ** k):
    if USCLN_1(n, int(i)) == 1:
        count += 1
        print(i, end=" ")
        if count % 10 == 0:
            print()
