# #in ra sl chu hoa chu thuong
# #F.1
# def xuly(a):
#     chuhoa = 0
#     chuthuong = 0
#     for i in range(len(a)):
#         if a[i].islower():
#             chuthuong += 1
#         elif a[i].isupper():
#             chuhoa += 1
#     print("so luong chua hoa: ", chuhoa, "\n" + "so luong chua thuong: ", chuthuong)
#
#
# a = input("")
# xuly(a)


# # danh sach in ra duy nhat
# # L.2
# def Xuly(a):
#     a = list(set(a))
#     print(a)
#
#
# a = [1, 2, 3, 2, 3, 3, 3, 4, 5, 5]
# Xuly(a)

# # So nguyen to b
# # L.3
# import math
#
#
# def isPrime(n):
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return n > 1
#
#
# n = int(input())
# print(isPrime(n))

# # dao nguoc chuoi
# # L.4
# def daoNguocChuoi(s):
#     s = s[::-1]
#     print(s)
#
#
# s = input()
# daoNguocChuoi(s)

# abc def ghk abd cbe


# # so lon nhat
# # L.5
# def SoLonNhat(lst):
#     print(max(lst))
#
#
# lst = [1, 4, 6, 2, 3, 5, 7, 0]
# SoLonNhat(lst)

# abc def ghk abd cbe
# L.6
def sapxepchuoi():
    a = input().split()
    print(sorted(a))
sapxepchuoi()