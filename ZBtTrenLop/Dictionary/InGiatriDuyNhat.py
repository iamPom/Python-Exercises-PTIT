a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
res = set()
for i in a:
    for j in i.values():
        res.add(j)
print(res)
