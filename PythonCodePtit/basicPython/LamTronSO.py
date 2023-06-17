t = int(input())
while t > 0:
    t -= 1
    lst = list(int(i) for i in input())
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] > 4:
            lst[i - 1] += 1
        lst[i] = 0
    for i in lst:
        print(i,end='')
    print()