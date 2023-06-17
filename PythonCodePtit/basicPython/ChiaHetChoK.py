a, k, n = input().split()
a, k, n = int(a), int(k), int(n)
count = 0
dau = k - (a % k)
for i in range(dau, n - a + 1, k):
    if (a + i) % k == 0:
        print(i, end=" ")
        count += 1

if count == 0:
    print("-1")
