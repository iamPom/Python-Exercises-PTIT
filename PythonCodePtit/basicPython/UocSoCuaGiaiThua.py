t = int(input())
while t > 0:
    t -= 1
    n, p = map(int,(input().split()))
    count = 0
    while n:
        n //= p
        count += n
    print(count)
 # for i in range(2,a+1):
 #        j = i
 #        while j%p ==0:
 #            s+=1
 #            j/=p