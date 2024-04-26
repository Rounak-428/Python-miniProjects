# cook your dish here
T = int(input())
for _ in T:
    n = int(input())
    for i in range(str(n)):
        if n%i == 0 and i != 1:
            print("yes")
            break
        
        elif n==1:
            print("yes")
            break
        
        else:
            print("no")
            break
        
