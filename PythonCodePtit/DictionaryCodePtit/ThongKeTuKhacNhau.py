import re
from collections import Counter

s = ""
for i in range(int(input())): s += (input() + " ")
for key, value in sorted(Counter(sorted(re.findall("\w+", s.lower()))).items(), key=lambda item: item[1], reverse=True):
    print(key, value)
