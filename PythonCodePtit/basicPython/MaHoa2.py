p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    s = input().split()
    k = int(s[0])
    if k == 0:
        break
    res = ""
    s = s[1]
    for i in s:
        index = p.find(i)
        res = p[(index + k) % 28] + res
    print(res)
