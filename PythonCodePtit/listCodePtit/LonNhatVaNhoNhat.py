while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        j=int(input())
        a.append(j)
    temp1 = min(a)
    temp2 = max(a)
    if temp1 == temp2:
        print("BANG NHAU")
    else:
        print(temp1, temp2)
