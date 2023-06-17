s = input()
i = len(s) - 1
count = 0
res = ""
while 1:
    count += 1
    res = s[i] + res
    if i == 0: break
    if count == 3:
        res = "," + res
        count = 0
    i -= 1
print(res)
