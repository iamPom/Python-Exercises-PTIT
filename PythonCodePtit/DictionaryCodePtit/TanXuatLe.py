# t = int(input())
# while t > 0:
#     t -= 1
#     n = int(input())
#     a = [int(i) for i in input().split()]
#     a.sort()
#     dem = 1
#     check = True
#     for i in range(len(a) - 1):
#
#         if a[int(i)] == a[int(i) + 1]:
#             dem += 1
#         elif dem % 2 == 1:
#             print(a[int(i)])
#             check = False
#             break
#         else:
#             dem = 1
#     if check:
#         print(a[-1])
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(int(i) for i in input().split())
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    print(dict)
    for i in dict.items():
        if i[1] % 2==0:
            print(i[0])
            break