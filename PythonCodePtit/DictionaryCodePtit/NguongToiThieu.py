a = input()
k = int(input())
s = {}
for i in range(1, len(a), 2):
    so = int(a[i - 1]) * 10 + int(a[i])
    if so not in s:
        s[so] = 1
    else:
        s[so] += 1
res = sorted(s.items(), key=lambda x: x[0])
check = True
for i in res:
    if i[1] >= k:
        print(i[0], i[1])
        check = False
if check:
    print('NOT FOUND')
