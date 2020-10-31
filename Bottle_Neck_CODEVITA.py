n=int(input())
i=[int (i) for i in input().split()]
j=(max(set(i),key=i.count))
print(i.count(j))
