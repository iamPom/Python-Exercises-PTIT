from collections import Counter

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = []
    for i in range(n):
        j = int(input())
        a.append(j)
    cnt = Counter(a)
    print(max(a, key=cnt.get))
    # print(cnt,cnt[0],cnt[1],cnt[3])
    # print(max(set(a), key=a.count))
