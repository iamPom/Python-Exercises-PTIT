n = input()
while int(n) > 10:
    index = len(n) // 2
    a = int(n[:index])
    b = int(n[index:])
    n = str(a + b)
    print(n)
