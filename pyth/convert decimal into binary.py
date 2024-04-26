n = int(input("Enter a number to convert it into binary form "))
k = n.split()
for i in k%2:
    if i==0:
        list.append(i)
    elif i==1:
        list.append(i)
    else:
        break

while i < len(list):
    list[i] = list[i+1]
    i=i+1
print(list)
    
    
