n = int(input())
arr = []
for i in range(n):
    s = input()
    tmp = []
    for j in s:
        tmp.append(j)
    arr.append(list(s))
print(arr)