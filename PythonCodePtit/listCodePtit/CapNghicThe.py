n = int(input())
a = []
a = [int(i) for i in input().split()]
count = 0
for i in range(n - 1):
    for j in range(i, n):
        if a[i] > a[j]:
            count += 1
print(count)
