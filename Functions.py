'''
function is a block of code to complete a specific task and it avoids rewriting the same code over and over
it is a reuable

1. built-in functions
2. user-defined functions

by using function two keywords use:

1. return (optional)
2. def (mandatory)

'''



def call():
    print("welcome to function")
call()
call()

def sum():
    a = 10
    b = 20
    sum = a+b
    print("sum is",sum)
sum()

def mul(a,b):
    m = a*b
    print("m is",m)
mul(10,20)
mul(20,30)

def student(name,age,grade):
    print("name is",name,"\n","age is",age,"\n","grade is",grade)
student("Rehan",20,'A')

def cube(n):
    return n*n*n
print("cube is",cube(3))

def square(num):
    sq = num*num
    return sq
s = square(4)
print("square is",s)


def outerfun():
    print("outer function")
    def innerfun():
        print("inner function")
    innerfun()
outerfun()

def name(firstname,lastname):
    print("fistname is",firstname,"lastname is",lastname)
name("ankit","gotam")

def eo(number):
    if (number%2==0):
        print(number,"is a even number")
    else:
        print(number,"is a odd number")
eo(5)
eo(4)



