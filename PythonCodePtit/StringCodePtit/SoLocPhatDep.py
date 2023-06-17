# def check(s):
#     if ('888' in s) or (s[0] == '8'):
#         return 'NO'
#     for i in s:
#         if i != '6' and i != '8':
#             return 'NO'
#     return 'YES' #ban hoa
n = input()
n = n.replace('688', "")
n = n.replace('68', '')
n = n.replace("6", '')
if len(n):
    print("NO")
else:
    print("YES")
