#perfect number

n= int(input("Enter the number to find it is a perfect number or not"))
t = n
i = 1
sum = 0
while i < t:
    if t%i == 0:
        sum += i
    i +=1

if sum == n:
    print("The number is perfect")

else:
    print("The number is not perfect")
