t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    ok = True
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            ok = False
            break
    if ok:
        print("YES")
''' 
2
4
7 5 3 2
5 4 8 7
8
7 5 3 2 5 105 45 10
2 4 0 5 6 9 75 84
'''
