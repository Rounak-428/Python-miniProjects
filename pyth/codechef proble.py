# cook your dish here

def gcd(a, b):
    if b > a:
        gcd(b, a)
        
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)
        
def lcm(a,b):
    k = gcd(a,b)
    return (k)*(a//(k))*(b//(k))
 
T = int(input())   
for _ in range(T):
    a,b = map(int, input().split())
    print(gcd(a,b), lcm(a,b))
