#an alternative for exercice 11
#answer on the console is on same line as the question
age = input("How old are you? ")
height = input("How tall are you ")
weight = input("How much do you weigh? ")

x = "So you are {} ".format(age)
y = "years old {} ".format(height)
z = "feets tall and {} ".format(weight)
a = "kgs heavy"

print(x + y + z + a)
