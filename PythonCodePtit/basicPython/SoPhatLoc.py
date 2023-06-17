#code:  	PY01020
t=int(input())
while t >0:
    t-=1
    b=str(input())
    if(b[len(b)-2]=='8' and b[len(b)-1]=='6'):
        print("YES")
    else:
        print("NO")