n = int(input())
a = [int(x) for x in input().split()]
num, step = a[0], sum(abs(x - a[0]) for x in a)
for i in range(1, n):
    t = sum(abs(x - a[i]) for x in a)
    if step > t:
        step = t
        num = a[i]
print(step, num)