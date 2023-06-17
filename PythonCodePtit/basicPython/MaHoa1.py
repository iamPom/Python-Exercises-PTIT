t = int(input())
while t > 0:
    t -= 1
    s = input()
    index = 0
    res = ""
    while index < len(s) - 1:
        count = 1
        while s[index] == s[index + 1]:
            count += 1
            index += 1
            if index == len(s) - 1:
                break
        res += str(count) + s[index]
        index += 1
    if s[len(s) - 1] != s[len(s) - 2]:
        res += "1" + s[len(s) - 1]
    if len(s) == 1:
        res += "1" + s[0]
    print(res)
