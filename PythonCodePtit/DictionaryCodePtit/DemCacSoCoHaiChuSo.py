n = input()
s = {}
for i in range(0, len(n), 2):
    temp = n[i:i + 2]
    if len(temp) <2: break
    if temp not in s:
        s[temp] = 1
    else:
        s[temp] += 1
for i in s.keys():
    print(i,s[i])
# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2