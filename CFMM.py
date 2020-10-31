t=int(input())
for q in range (t):
    n=int(input())
    s=''
    for i in range(n):
        s+=input()
    c=s.count("c")//2
    o=s.count("o")
    d=s.count("d")
    e=s.count("e")//2
    h=s.count("h")
    f=s.count("f")
    print(min(c,o,d,e,h,f))
