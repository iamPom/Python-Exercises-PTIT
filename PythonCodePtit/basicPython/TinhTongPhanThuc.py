t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    sum = 0.0
    for i in range(2 - n % 2, n + 1, 2):
        sum += 1.0 / i
    print("{:.6f}".format(sum))
# round(sum, 6)