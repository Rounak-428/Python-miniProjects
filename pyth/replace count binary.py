T = int(input())
for _ in range(T):
    s = input()
    if len(s)==1:
        print(0)
    else:
        ze=0
        on=0
        for i in s:
            if i=='1':
                on+=1
            elif i=='0':
                ze+=1
        if (ze==on):
            print(0)
        elif (ze>on):
            print(on)
        elif (on>ze):
            print(ze)
    
