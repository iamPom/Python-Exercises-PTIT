# t=int(input())
# a=[]
# while t:
#     t-=1
#     n=input().split()
#     for i in range(len(n)):
#         if n[i].isdigit():
#             a.append(n[i])
# tong=0
# tich=1
# for i in range(len(a)):
#     tong+=int(a[i])
#     tich*=int(a[i])
# print(tong, tich)

# n, k = map(int, input().split())
# def check(a,b):
#     sum=0
#     for i in range(a):
#         if a % i ==0:
#             sum+=i
#     if sum !=b: return False
#     sum=0
#     for i in range(b):
#         if b % i ==0:
#             sum+=i   
#     if sum !=a: return False
#     return True
# n, k = map(int, input().split())       
# if check(n,k):
#     print("YES")
# else: print("NO")
n=int(input())
a = [int(i) for i in input().split()]
b= []
sum=0
for i in range(len(a)):
    sum+=a[i]
    b.append(sum)
tong=0
tich=1
for i in range(len(b)):
    tong+=int(b[i])
    tich*=int(b[i])
print(tong, tich)