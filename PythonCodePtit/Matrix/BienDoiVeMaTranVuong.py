row, col = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(row)]
tmp = 0 if row > col else 1
pos = []
for _ in range(abs(row - col)):
    pos.append(tmp)
    tmp += 2
for r in range(row):
    if (row > col and r not in pos) or row == col:
        print(*a[r])
    elif row < col:
        for c in range(col):
            if c not in pos: print(a[r][c], end=' ')
        print()