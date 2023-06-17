# bai LA 1
def bai1():
    list1 = [-1, 2, -3, 5, 7, 8, 9, -10]
    list2 = list(filter(lambda x: x > 0, list1))
    list3 = list(filter(lambda x: x < 0, list1))
    list2.sort()
    list3.sort()
    list4 = list2 + list3
    print("bai 1:", list4, "\n")
# bai2


def bai2():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result = list(map(lambda x, y: x + y, list1, list2))
    print("bai 2:", result, "\n")
# bai3


def bai3():
    list1 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
    list2 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, list1))
    print("bai 3:", list2, "\n")
# bai4


def bai4():
    list1 = ['php', 'w3r', 'python', 'abcd', 'java', 'aaa']
    list2 = list(filter(lambda x: x == x[::-1], list1))
    print("bai 4:", list2, "\n")
# bai5


def bai5():
    list1 = [2, 4, -6, -9, 11, -12, 14, -5, 17]
    list2 = list(filter(lambda x: x > 0, list1))
    list3 = list(filter(lambda x: x < 0, list1))
    print("bai 5:", sum(list2), sum(list3), "\n")


bai1()
bai2()
bai3()
bai4()
bai5()
