# a = []
# index = 10
# while index > 0:
#     n = input()
#     s = ""
#     s += n
#     n += " "
#     a += s.split()
#     index = 10 - len(a)
# setA = set()
# for i in a:
#     setA.add(int(i) % 42)
# print(len(setA))

a=[]
s=set()
for i in range(10):
    n=int(input())
    a.append(n)
for i in a:
    s.add(i%42)
print(len(s))