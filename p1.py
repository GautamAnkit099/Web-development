'''
num1 = 4
num2 = num1 + 1
num1 = 2
print(num1,num2)
'''
'''
num1,num2 = 2,6
num1,num2 = num2,num1 + 2
print(num1,num2)
'''

'''

flow of control

1. selection or decision making or conditional statements (if else)
2. Iterative statements(loops : for,while)
3. transfer statements (break, continue)

'''

'''

if else statements:

age = int(input("enter age\n"))
if age>18:
     print(age,"you can vote")
else:
         print("your age is",age,"you can not vote")




marks = 90
if marks>=90:
    print("grade A")
elif marks>80:
    print("grade B")
else:
   print("grade C")
'''


'''

Loops :

loop is a repeatition


loop contains three things

1. initialization
2. condition
3. increment/decrement

1. for loop
2. while loop


'''

print("for loop")
for i in range(1,5):
    print(i)

print("\n")

num = 5
for j in range(1,num):
    print(j)


print("\n")
print("while loop")
z = 1 # initialization
while z<=5: # condition
    print(z)
    z = z+1 # increment
print("\n")
x = 10
while x>=1:
    print(x)
    x = x - 1
