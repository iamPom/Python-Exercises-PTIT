t=int(input())
while t >0:
    t-=1
    s=input()
    for i in range(0,len(s)-1,2):
        a=int(s[i+1])
        while a>0:
            print(s[i],end="")
            a-=1        
    print()