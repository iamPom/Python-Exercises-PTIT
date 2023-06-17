# code: PY01024
def tongCso(a):
    a = int(a)
    sum = 0
    while a > 0:
        sum += int(a % 10)
        a /= 10
    if sum % 10 == 0:
        return 1
    else:
        return 0


def deuNhau(s):
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    s = input()
    if tongCso(s) == 1 and deuNhau(s) == True:
        print("YES")
    else:
        print("NO")
