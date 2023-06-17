s = input()
countUp = 0
countDown = 0
for i in range(0, len(s)):
    if s[i].isupper():
        countUp += 1
    else:
        countDown += 1
if (countUp > countDown):
    print(s.upper())
else:
    print(s.lower())
