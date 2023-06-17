import re
from collections import Counter

n, k = map(int, input().split())
s = ""
for _ in range(n): s += (input().lower() + " ")
for key, value in sorted(Counter(sorted(re.findall(r"\w+", s))).items(), key=lambda item: item[1], reverse=True):
    if value >= k: print(key, value)