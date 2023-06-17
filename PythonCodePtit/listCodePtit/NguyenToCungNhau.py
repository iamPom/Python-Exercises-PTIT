def USCLN_1(a, b):
    if b == 0:
        return a
    return USCLN_1(b, a % b)


n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if USCLN_1(a[i], a[j]) == 1:
            print(a[i], a[j])
