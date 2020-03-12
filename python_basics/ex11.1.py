print("How old are you?")
age = int(input())  #you can use int(input())
print("How tall are you?")
height = input()
print('How much do you weigh?')
weight = input()


x = "so you are {}".format(age)
y = " years old {}".format(height)
z = " feets tall and {}".format(weight)
a = "Kgs heavy"

print(x+y+z+a)
