x = lambda a,b : a+b
print(x(20,10))

m = lambda n : n
print(m(50))

p = lambda x,y: x*y
print(p(20,30,))

ex = lambda c,d,e,f,g : c+d-e*f/g
print(ex(2,3,4,6,8))

def square(n):
    return lambda a : a*n
myfun = square(60)
myfun2 = square(70)
print(myfun(30))
print(myfun2(80))

'''

1. local variable : we declare inside the function
2. global variable : we declare outside of the function and we access local variable by using global keyword


'''

z = 20 # global variable
s = 40
def scope():
    z = 10 # local variable
    print(z)
    print(s)

global h
h = 50    
scope()
 # print(z)
print(z)
print(h)

