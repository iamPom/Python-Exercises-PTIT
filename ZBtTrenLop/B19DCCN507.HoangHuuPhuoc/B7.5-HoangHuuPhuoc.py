#Bài 7.5 - B19DCCN507 Hoàng Hữu Phước
def description_city(city, country):
    print(city, "is in", country)


city1 = "Manchester"
country = "English"
print("thanh pho 1: ")
description_city(city1, country)
print("Nhap ten thanh pho:")
city2 = input()
print("thanh pho 2: ")
description_city(city2, country)
print("thanh pho 3: ")
description_city(input(), country)