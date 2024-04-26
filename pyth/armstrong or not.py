#armstrong
original = int(input("Enter the number to find it is palindrome or not "))
num = original
sum = 0
while num > 0:
    sum = sum + (num%10) **3
    num = num//10

if sum ==original:
    print("The number is an armstrong number")

elif sum != original: print("The number is not armstrong number")
