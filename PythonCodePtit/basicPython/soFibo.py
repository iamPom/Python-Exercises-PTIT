# code:
t = int(input())
while t > 0:
    t -= 1
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == 1:
        print("1 1", end=' ')
    elif a == 2:
        print("1", end=' ')
    f1 = 1
    f2 = 1
    fn = 1
    count = 3
    while count <= b:
        f1 = f2
        f2 = fn
        fn = f1 + f2
        if count >= a:
            print(fn, end=' ')
        count += 1
    print()
