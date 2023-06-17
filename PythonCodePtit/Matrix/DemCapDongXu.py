n = int(input())
a = []
for i in range(n):
    a.append(list(input()))
res = 0
for i in range(n):
    count = 0
    for j in range(n):
        if a[i][j] == 'C':
            res += count
            count += 1
# tinh so theo hang, 1+2+3+... la tổ hợp chập 2 theo n
for j in range(n):
    count = 0
    for i in range(n):
        if a[i][j] == 'C':
            res += count
            count += 1
print(res)