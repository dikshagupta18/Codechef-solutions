t=int(input())
for q in range(t):
    a,b=map(int, input().split())
    a1,b1=1,2
    s1,s2=a1,b1
    flag=0
    while(True):
        if s1>a:
            flag=1
            break
        if s2>b:
            flag=2
            break
        a1+=2
        b1+=2
        s1+=a1
        s2+=b1
    if flag==1:
        print("Bob")
    elif flag==2:
        print("Limak")
