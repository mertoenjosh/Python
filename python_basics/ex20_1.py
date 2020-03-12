def add(a, b):
    print("ADDING {}".format(a + b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING {}".format(a - b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING {}".format(a * b))
    return a * b

 def divide(a, b):
     print("DIVIDING {}".format(a / b))
     return a / b


print("Let's do some math with just functions!")

age = add(15, 4)
height = subtract(66, 9)
weight = multiply(30, 2)
iq = divide(50, 0.5)

print("Age: {}".format(age)," Height: {}".format(height)," weight: {}".format(weight)," IQ: {}".format(iq))


#a puzzle
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
