t = int(input())
while t > 0:
    t -= 1
    check = True
    n, m, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    i = j = l1 = 0
    while i < n and j < m and l1 < k:
        if a[i] == b[j] and a[i] == c[l1]:
            print(a[i], end=' ')
            check = False
            i += 1
            j += 1
            l1 += 1
            continue
        if a[i] < b[j] or a[i] < c[l1]:
            i += 1
            continue
        if b[j] < a[i] or b[j] < c[l1]:
            j += 1
            continue
        if c[l1] < a[i] or c[l1] < b[j]:
            l1 += 1
            continue
    if check:
        print("NO")
    print()
