t = int(input())
while t > 0:
    t -= 1
    s = input()
    res = ""
    sum = 0
    for i in s:
        if i.isalpha():
            res += i
        else:
            sum += int(i)
    print("".join(sorted(res)) + str(sum))
