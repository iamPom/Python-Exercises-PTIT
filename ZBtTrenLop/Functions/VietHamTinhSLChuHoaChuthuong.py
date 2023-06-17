def xuly(a):
    chuhoa = 0
    chuthuong = 0
    for i in range(len(a)):
        if a[i].islower():
            chuthuong += 1
        elif a[i].isupper():
            chuhoa += 1
    print("so luong chua hoa: ", chuhoa, "\n" + "so luong chua thuong: ", chuthuong)


a = input("")
xuly(a)
