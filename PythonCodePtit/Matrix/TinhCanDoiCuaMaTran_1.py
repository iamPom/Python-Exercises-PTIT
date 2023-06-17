n = int(input())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))
k = int(input())
sumabove = 0  # sum trên
sumbelow = 0  # sum dưới
for i in range(n):
    for j in range(n):
        if j > i: sumabove += a[i][j]
        if j < i: sumbelow += a[i][j]
if abs(sumabove - sumbelow) > k:
    print('NO')
else:
    print("YES")
print(abs(sumabove - sumbelow))
