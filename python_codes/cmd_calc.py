import os
os.system("clear")

def addition(x, y):
    answer = x+y
    return answer

def subtraction(x, y):
    answer = x-y
    return answer

def multiplication(x, y):
    answer = x*y
    return answer

def division(x, y):
    answer =x/y
    return answer

try:
    first = float(input("Enter First number:\n>> "))

    second = float(input("Enter second number:\n>> "))

    s = input("Enter a sign operand  (+-/*)\n ")

    if s == '+':
        print(addition(first, second))

    elif s == '-':
        print(subtraction(first ,second))

    elif s == '*' or 'x':
        print(multiplication(first, second))

    elif s == '/' or '\\':
        print(division(first, second))

    else:
        print("Enter a valid sign or number")
except:
    print("Enter a number")
