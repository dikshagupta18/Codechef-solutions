for _ in range(int(input())):
    s=input()
    b=0
    mb=0
    st=''
    for i in s:
        if i == '(':
            b += 1
        if i == ')':
            b -=1
        mb=max(b, mb)
    for x in range(mb):
        st+='('
    for x in range(mb):
        st+=')'
    print(st)
