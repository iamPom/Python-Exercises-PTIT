t = int(input())
res = []
while t > 0:
    t -= 1
    s = input()
    for i in s:
        if i.isalpha():
            s = s.replace(i, " ")
    s = s.split()
    for i in s:
        res.append(int(i))
res.sort()
for i in res:
    print(i) 