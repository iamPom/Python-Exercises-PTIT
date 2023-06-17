def doiCoSo(x, k):
    res = ''
    while x:
        res = arr[x % k] + res
        x //= k
    print(res)


t = int(input())
while t:
    t-=1
    arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n, b = map(int, input().split())
    doiCoSo(n, b)
