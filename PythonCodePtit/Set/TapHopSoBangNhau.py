a = [int(x) for x in input().split()]
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}
if set1 == set2:
    print("YES")
else:
    print("NO")
