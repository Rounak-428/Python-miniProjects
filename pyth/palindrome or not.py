#palindrome
orig=int(input("Enter the number to find wether its palindrome or not"))
num=orig
rev = 0
while num >0:
    
    digit = num % 10
    rev = rev*10 + digit
    num = num//10
if rev == orig:
    print("The number is a palindrome")
else: print("The number is not a palindrome")

    

