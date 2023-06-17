# code:
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    b = int(n / 2)
    a = [int(i) for i in input().split()]
    a.sort()
    max = 1
    index = a[0]
    count = 1
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            count += 1
            if count > max:
                max = count
                index = a[i]
        else:
            count = 1
    if max >= b:
        print(index)
    else:
        print("NO")
