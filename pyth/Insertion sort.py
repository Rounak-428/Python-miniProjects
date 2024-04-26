#Insertion sort
l=[67,54,67,23,98,43]

for i in l:
    j=l.index(i)
    while j>0:
        
        if l[j] < l[j-1]:
            l[j] , l[j-1] = l[j-1] , l[j]

        else:
            break
        j=j-1

print(l)
