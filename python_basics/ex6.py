#using the dot format() syntax.. and the f-string format
#we are using the f-string format to call for the declare variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#displaying value of x and y that is the initialized statements
print(x)
print(y)
#printing the value of x again
print(f"I said: {x}")
#printing value of Y but presense of single quotes makes curious
print(f"I also said: '{y}''")
#initialize hilarious to be false

hilarious = False#False is without quotes and F is capital
#initializing joke_evaluation leaving empty curry brakets
joke_evaluation = "Isn't that joke funny?!{}"
#print initialized function joke_evaluation and format hilarious using .format()
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
