n = int(input())
a = [float(x) for x in input().split()]
a.sort()
i = 1
j = len(a) - 2
sum = 0
while a[i - 1] == a[i]: i += 1
while a[j + 1] == a[j]: j -= 1
for l in range(i, j + 1):
    sum += a[l]
print('{:.2f}'.format(sum / (j + 1 - i)))
