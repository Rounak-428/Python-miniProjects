import pickle

file1 = open('text1.txt', 'w')
file2 = open('text2.txt', 'w')
file1.write("How are you in the holy world")

file = open('text.txt', 'r')
pickle.load(file1,file)
pickle.load(file,file2)

drift = file2.readline()
print(drift)
file.close()
file1.close()
file2.close()
