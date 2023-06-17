while True:
    a = [int(i) for i in input().split()]
    if a[1] == a[2] == a[3] == a[0] == 0:
        break
    count = 0
    while True:

        if a[1] == a[2] == a[3] == a[0]:
            print(count)
            break
        c = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - c)
        count += 1
