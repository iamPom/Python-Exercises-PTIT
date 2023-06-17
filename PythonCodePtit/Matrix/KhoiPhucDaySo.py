def sol():
    n = int(input())
    a = []
    for _ in range(n):
        a.append([int(x) for x in input().split()])
    if n == 2: return [a[0][1] // 2] * 2
    b = [ (a[0][1] + a[0][2] - a[1][2]) // 2 ]
    for i in range(1, n):
        b.append(a[0][i] - b[0])
    return b

# drive code
print(*sol())