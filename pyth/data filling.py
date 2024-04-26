def bin_file():
    import pickle
    f= open('data1.dat', 'wb')

    while True:
        x= int(input("Enter the integer :"))
        pickle.dump(x, f)
        ans  = input("Want to add more data, Y/N ?")
        if ans.upper() != 'Y' or ans.upper() != 'N':
            ans = input("Want to add more data, Y/N ?")
        elif ans.upper() == 'N':break
        
    f.close()
    f = open('data1.dat', 'rb')
    try:
        while True:
            var = pickle.load(f)
            print(var)
    except EOFError:
        pass
    f.close()

bin_file()

    
