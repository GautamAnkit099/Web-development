'''

selection or conditional or decision making statements

syntax:

variable_name = value

if condition:

statements

1. simple if
2. if else
3. if elif
4. Nested if else

'''
# simple if


num = 10

if num>1:
    print("this is a if part..")


# if else

name ="Loop"

if "Loop"!="Loop":
    print("if part")
else:
    print("else part")


# Nested if elif

    marks = 90
    if marks>90:
        print("grade A")
    elif marks==80:
            print("grade B")
    elif marks<=80:
            print("grade C")
    else:
            print("fail")
            
# Nested if else


num2 = 99
if num2>99:
    print("number is 98")
else:
        if num2!=99:
            print("number is 99")
        else:
                print("this is not a number")


num3 = 96
if num3>=96:
    print("A")
    if num3>96:
        print("number is not 96")
    else:
            print("number is 96")
else:
                print("this is a number")
