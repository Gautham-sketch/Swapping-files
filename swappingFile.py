def swapFile ():
    textInput = input("Enter your file name :- ")

    with open(textInput,'r') as a:
        data_a = a.read()
    with open(textInput,'r') as b:
        data_b = b.read()
    with open(textInput,'w') as a:
        a.write(data_b)
    with open(textInput,'w') as b:
        b.write(data_a)
swapFile()   