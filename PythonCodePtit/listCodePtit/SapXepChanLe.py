n = int(input())
count = 0
a = []
while count < n:
    line = [int(i) for i in input().split()]
    for i in line:
        count += 1
    a.extend(line)
chan = []
le = []
res = []
for i in a:
    if i % 2:
        le.append(i)
    else:
        chan.append(i)
le = sorted(le, reverse=True)
chan.sort()
ichan = 0
ile = 0
for i in a:
    if i % 2:
        print(le[ile], end=' ')
        ile += 1
    else:
        print(chan[ichan], end=' ')
        ichan += 1


# N = int(input())
# le = []
# chan = []
# sl = 0
# arr = []
# while sl < N:
#     arrtmp = list(int(i) for i in input().split())
#     for so in arrtmp:
#         sl = sl + 1
#         if so % 2 != 0:
#             le.append(so)
#         else:
#             chan.append(so)
#     arr.extend(arrtmp)
# le.sort(reverse=True)
# chan.sort()
# i = 0
# j = 0
# for x in arr:
#     if x % 2 != 0:
#         print(le[i], end = ' ')
#         i = i + 1
#     else:
#         print(chan[j], end =' ')
#         j = j + 1
# print()