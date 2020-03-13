import os
os.system("clear")
def get_power(base, power):
    result = 1
    for number in range(power):
        result = result * base
    return result
try:
    num1 = int(input("Enter base number: "))
except NameError, SyntaxError:
    print('''\v\tPlease check your first number
                its been initialized as \"0\" \v''')
    num1 = 0
try:
    num2 = int(input("Enter power number: "))
except NameError, SyntaxError:
    print('''\v\tPlease check your second number
                its been initialized as \"0\" \v''')
    num2 = 0



final = (get_power(num1, num2))
print("{} power {} is {}".format(num1, num2, final))
