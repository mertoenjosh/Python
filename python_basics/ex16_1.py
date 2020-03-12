#need to carefully review this
from sys import argv

script, filename = argv
#why is return and  ^c not working..
#work on that
print("We're going to erase {}.".format(filename))
print("If you don't want that, hit CTLR-C (^C).")
print("If you don't want that hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')#read about that 'w'

print("Truncating the file. Goodbye!")
target.truncate()
#simplify the code as much as possible
print("Now am going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#try writing using only one line of code this part
#hint: use strings, formats and escapes
print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#we are closing the file now
print("And finally we close it.")
target.close()

#we are reopening the file to edit its contents
target = open(filename)
print(target.read())
