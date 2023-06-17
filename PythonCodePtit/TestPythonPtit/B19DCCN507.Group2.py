# Bài L.1
print("Bai L1:")
# a1 = [int(i) for i in input("Nhap cac ptu list cach nhau 1 khoang trang: ").split()] #neu muon nhap
a1 = [1, 3, 5, 7, 4, 1, 6, 8]  # neu cho luon khong phai nhap
le = 0
chan = 0
if int(a1[0]) % 2 == 0:
    chan = a1[0]
else:
    le = a1[0]
if chan == 0:
    for i in a1:
        if int(i) % 2 == 0:
            chan = i
            break
else:
    for i in a1:
        if int(i) % 2 == 1:
            le = i
            break
print("So chan va le dau tien xuat hien la:", chan, le)
print()

# Bài L.2
print("Bai L2:")
a2 = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
l2 = 8
r2 = 10
print("Tong cac so tu chi so " + str(l2) + " den " + str(r2) + " la: ", sum(a2[int(l2):int(r2) + 1]))
print()

# Bài L.3
print("Bai L3:")
s3 = ['Red', 'Green', 'Blue', 'White', 'Black']
res3 = []
for i in s3:
    i = i[::-1]
    res3.append(i)
print("Dao chuoi tung phan tu:", res3)
print()

# Bài L.4
print("Bai L4:")
a4 = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
res4 = []
for i in a4[0]:
    check = True
    for j in range(1, len(a4)):
        if i not in a4[int(j)]:
            check = False
            break
    if check:
        res4.append(i)
res4.reverse()  # e in ra theo output cua thay a
print("Phan tu chung cua danh sach long nhau:", res4)
print()

# Bài L.5
print("Bai L5:")


def ktraDuyNhat(x5):
    for i in x5:
        if x5.count(int(i)) > 1:
            return False
    return True


a5_1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
print("Kiem tra duy nhat mang thu nhat:", end=" ")
if ktraDuyNhat(a5_1):
    print("True")
else:
    print("False")
a5_2 = [2, 4, 6, 8, 10, 12, 14]
print("Kiem tra duy nhat mang thu hai:", end=" ")
if ktraDuyNhat(a5_2):
    print("True")
else:
    print("False")
print()

# Bài L.6
print("Bai L6:")


def ktraSapXep(x6):
    y6 = list(x6)
    y6.sort()
    if y6 == x6:
        return True
    else:
        return False


a6_1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print("Kiem tra sap xep mang thu nhat:", end=" ")
if ktraSapXep(a6_1):
    print("True")
else:
    print("False")
a6_2 = [1, 2, 4, 8, 6, 10, 12, 14, 16, 17]
print("Kiem tra sap xep mang thu hai:", end=" ")
if ktraSapXep(a6_2):
    print("True")
else:
    print("False")
print()

# Bài L.7
print("Bai L7:")
a7 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
max7 = 1
s = set()
for i in a7:
    if a7.count(i) > max7:
        max7 = a7.count(i)
for i in a7:
    if a7.count(i) == max7:
        s.add(i)
print("Nhung muc co so lan xuat hien toi da:", end=' ')
for i in s:
    print(i, end=" ")
print()
print()

# Bài L.8
print("Bai L8:")
a8_1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("Kiem tra danh sach thu nhat:")
cot8_1 = 1
res8_1 = []
print("Cot thu " + str(cot8_1) + " la:", end=' ')
for i in range(len(a8_1)):
    res8_1.append(a8_1[int(i)][cot8_1 - 1])
print(res8_1)
a8_2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print("Kiem tra danh sach thu hai:")
cot8_2 = 3
res8_2 = []
print("Cot thu " + str(cot8_2) + " la:", end=' ')
for i in range(len(a8_2)):
    res8_2.append(a8_2[int(i)][cot8_2 - 1])
print(res8_2)
print()

# Bài L.9
print("Bai L9:")
a9_1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
cot9_1 = 1
print("Xoa cot thu " + str(cot9_1) + " khoi danh sach thu nhat: ")
for i in range(len(a9_1)):
    a9_1[int(i)].pop(cot9_1 - 1)
print(a9_1)
a9_1 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
cot9_1 = 3
print("Xoa cot thu " + str(cot9_1) + "  khoi danh sach thu hai: ")
for i in range(len(a9_1)):
    a9_1[int(i)].pop(cot9_1 - 1)
print(a9_1)
print()

# Bài L.10
print("Bai 10:")
print("Sap xep hang theo thu tu tang dan cua tong ma tran thu 1: ")
a10 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
v = []
for i in range(0, len(a10)):
    v.append([sum(a10[int(i)])])
    for j in range(0, len(a10[int(i)])):
        v[int(i)].append(a10[int(i)][int(j)])
v.sort()
for i in range(len(v)):
    v[int(i)].pop(0)
print(v)
print("Sap xep hang theo thu tu tang dan cua tong ma tran thu 2: ")
a10 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
v = []
for i in range(0, len(a10)):
    v.append([sum(a10[int(i)])])
    for j in range(0, len(a10[int(i)])):
        v[int(i)].append(a10[int(i)][int(j)])
v.sort()
for i in range(len(v)):
    v[int(i)].pop(0)
print(v)
print()
print("Good luck!...end")
