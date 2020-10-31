t=int(input())
for q in range(t):
    n=int(input())
    li=[input().split() for i in range(n)]
    di={}
    for a,b in li:
        if a in di:
            di[a]+=1
        else:
            di[a]=1
    for a,b in li:
        if di[a]==1:
            print(a)
        else:
            print(a,"",b)
       
