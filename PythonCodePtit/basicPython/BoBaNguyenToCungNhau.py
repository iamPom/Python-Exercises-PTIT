def USCLN(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a %= b
    return b


l, r = map(int, input().split())
count = 0
for i in range(l, r - 1):
    for j in range(i + 1, r):
        if USCLN(int(i), int(j)) != 1:
            continue
        for k in range(j + 1, r + 1):
            if USCLN(int(i), int(k)) == 1 and USCLN(int(j), int(k)) == 1:
                print("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")
