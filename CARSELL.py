for _ in range(int(input())):
    n=int(input())
    li=list(map(int, input().split()))
    li.sort(reverse=True)
    for x in range(n):
        if li[x]>x:
            li[x]-=x
        else:
            li[x]=0
    print(sum(li)%1000000007)
