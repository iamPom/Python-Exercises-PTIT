row, col = map(int, input().split())
a = [[int(j) for j in input().split()] for i in range(row)]
nummax = a[0][0]
nummin = a[0][0]
for i in range(row):
    if nummax < max(a[i]):
        nummax = max(a[i])
    if nummin > min(a[i]):
        nummin = min(a[i])
res = nummax - nummin
check = True
for i in range(row):
    for j in range(col):
        if a[i][j] == res :
            if check:
                print(res)
                check = False
            print("Vi tri ["+str(i)+"]["+str(j)+"]")
if check:
    print("NOT FOUND")