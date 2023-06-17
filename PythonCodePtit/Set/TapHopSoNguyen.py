def inRa(x):
    for i in x:
        print(i, end=" ")
    print()


a, b = input().split()
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}
giao = list(set1.intersection(set2))
hieu1 = list(set1.difference(set2))
hieu2 = list(set2.difference(set1))
giao.sort()
hieu1.sort()
hieu2.sort()
inRa(giao)
inRa(hieu1)
inRa(hieu2)
