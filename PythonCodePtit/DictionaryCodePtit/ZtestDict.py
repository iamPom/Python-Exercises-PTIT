import re

T = int(input())
word = []
for t in range(T):
    s = input()
    word.extend(re.findall(r'\w+', s))
print(word)
dict = {}
for i in word:
    if len(i) == 0: continue
    if i.lower() not in dict:
        dict[i.lower()] = -1
    else:
        dict[i.lower()] -= 1
res = sorted(dict.items(), key=lambda x: (x[1], x[0]))
for i in res:
    print(i[0] + " " + str(0 - int(i[1])))
