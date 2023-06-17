def USCLN_1(a, b):
    if b == 0:
        return a
    return USCLN_1(b, a % b)


t = int(input())
while t > 0:
    t -= 1
    s = input()
    s1 = s[::-1]
    if USCLN_1(int(s),int(s1))==1:
        print("YES")
    else: print("NO")