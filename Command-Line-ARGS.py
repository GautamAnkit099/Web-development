from sys import argv
print("the number of command line arguments",len(argv))
print("The list of command line argument",argv)
print("command line arguments one by one")
for i in argv:
    print(i)
