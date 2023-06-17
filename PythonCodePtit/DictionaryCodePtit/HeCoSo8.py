def decToOctober(x):
    dict1 = {
        '000': '0',
        '001': '1',
        '010': '2',
        '011': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7',
    }
    return dict1[x]


s = input()
while len(s) % 3:
    s = "0" + s
res = ''
for i in range(0, len(s), 3):
    tmp = s[int(i):int(i) + 3]
    res = res + decToOctober(tmp)
print(res)

#print(oct(int(input(), 2))[2:]) #1 dòng ra đáp án

# lst = ["000", "001", "010", "011", "100", "101", "110", "111"]
#
# def cs(n):
#     for i in range(len(lst)):
#         if n == lst[i]:
#             return i
#
# def run():
#     n = input()
#     if len(n) % 3 == 2:
#         n = "0" + n
#     if len(n) % 3 == 1:
#         n = "00" + n
#     tmp = ""
#     res = ""
#     for i in range(len(n)):
#         tmp += n[i]
#         if len(tmp) == 3:
#             res += str(cs(tmp))
#             tmp = ""
#     print(res)
#
# run() #Diep
