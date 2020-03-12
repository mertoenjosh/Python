#its like the curry brakets are creating a space to place something in them
#more of an array...
formatter = "{} {} {} {}"#initializing variable 'formatter'

#using a function to turn formatter variable into strings
print(formatter.format(1, 2, 3, 4))#i tried to add a fifth value and it was not displayed on the terminal
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

print(formatter.format(formatter, formatter, formatter, formatter))
print("{} {}" * 16)#I added this cool stuff
print(formatter.format(
    "All will",
    "be lost as",
    "tears in the rain",
    "as said by anonymous"
))
