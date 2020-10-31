for _ in range(int(input())):
    s=input()
    if s.startswith('1') and s.count('0')==len(s)-1:
        print('WIN')
    elif len(s)%2==0:
        if s.startswith('1') and s.endswith('1'):
            if s.count('1')==len(s):
                print('LOSE')
            else:
                print('WIN')
    elif len(s)%3==0 and s.count('1')==len(s):
        print('WIN')
