data = [10,20,30,40,50]
b = bytearray(data)
for i in data:
    print(i)
b[4] = 60
for i in b:
    print(i)
    x = [1,256]
    b = bytearray(x)
    print(b)
