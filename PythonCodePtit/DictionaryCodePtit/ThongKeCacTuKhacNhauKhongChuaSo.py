import re
from collections import Counter
s = ""
for _ in range(int(input())): s += (input().lower() + " ")
for key, value in sorted(Counter(sorted(re.findall(r"[a-zA-Z]+", s))).items(), key=lambda item: item[1], reverse=True):
    print(key, value)