# code:  	PY01012
s1 = input()
s2 = input()
b = list(s1)
s3 = int(input())
b.insert(s3 - 1, s2)
for i in range(0, len(b)):
    print(b[i], end='')
