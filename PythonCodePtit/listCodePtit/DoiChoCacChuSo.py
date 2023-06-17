def sol():
    n = list(input())
    ln = len(n)
    for i in range(ln - 2, -1, -1):
        if n[i] > n[i + 1]:
            maxV, idx = n[i + 1], i + 1
            for j in range(i + 2, ln):
                if n[i] > n[j] > maxV and n[j] < n[i]:
                    maxV = n[j]
                    idx = j
            n[idx], n[i] = n[i], n[idx]
            return '-1' if n[0] == '0' else ''.join(n)
    return -1


for _ in [0] * int(input()):
    print(sol())
