def sumNumber(x):
    x = str(x)
    sum = 0
    i = 0
    if x[0] == '-':
        sum += ord('-') - ord('0')
        i = 1
    while i < len(x):
        sum += int(x[i])
        i += 1
    return sum


n = input()
count = 1
while True:
    n = sumNumber(int(n))
    if int(n) < 10: break
    count += 1
print(count)
