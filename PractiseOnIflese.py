
'''
name = input("enter name")
print("my name is",name)
num = int(input('enter any  number'))
print(num)
num2 = float(input("enter any number"))
print(num2)
Bool = bool(input("enter True or False"))
print(Bool)

'''

data = '''
this is a python
programming
language
'''

print(data)
'''
str = ' this
is
a programming language'
print(str)

'''
'''
data2 = "this is a
language
to learn
quickly
"
'''


data3 = """this is a python
programming
language
"""
print(data3)



print("this is a 'python programming' language")
print('python is a "high level" programming language')
print("this is a logic""to create thing")
print("python","is a ","high level language")
print("python\" is a language")
print("this is a\n programming language")
print("python is a programming \tlanguage")
str1 = "hello"
str2 = "python"
print(str1,"\t",str2)

'''
sep as a separator
end as a occupy space
'''

print(str1,str2,end='')
print(str1,str2,sep='+')


num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))
if num1>num2 and num1>num3:
    print(num1,"is a greater number")
elif num2>num1 and num2>num3:
        print(num2,"is a greater number")
else:
            print(num3,"is a greater number")




            marks = 90
            if marks==98:
                print("first division")
            elif marks==99:
                    print("second division")
            elif marks==96:
                        print("third division")
            else:
                            print("falied")

