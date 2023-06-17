d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
for i in d1.keys():
    if i in d2.keys():
        d2[i] += d1[i]
    else: d2[i] = d1[i]
print(d2)