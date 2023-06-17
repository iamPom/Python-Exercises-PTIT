n = input()
s = {}
for i in range(2, len(n), 2):
    s[n[i - 2:i]] = 1
for i in s.keys():
    print(i, end=' ')
