# Bài 7.12 - B19DCCN507 Hoàng Hữu Phước
def sandwiches(*thanh_phan):
    for i in thanh_phan:
        print(str(i[0]) + ": ", i[1])
    print("Ket thuc don hang" + "\n")


print("Don Hang: ")
sandwiches(('Trung', '1 qua'), ('Tom', '2 con'), ('rau', 'nhieu'))
sandwiches(('Pho Mai', 'it'), ('Bơ', 'nhieu'),('Trung', '2 qua'))
sandwiches(('Thit Bo', '1 mieng'), ('Rau thom', 'it'),)
