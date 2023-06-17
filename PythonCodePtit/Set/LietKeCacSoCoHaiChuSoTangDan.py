n = input()
s = {}
a = set()
for i in range(0, len(n), 2):
    temp = n[i:i + 2]
    if len(temp) < 2: break
    if temp not in a:
        a.add(int(temp))
print(a)
a = list(a)
a.sort()
for i in a:
    print(i, end=' ')
#     if temp not in s:
#         s[temp] = 1
#     else:
#         s[temp] += 1
# for i in s.keys():
#     print(i, s[i])
