from sys import argv

script, filename = argv

print(f"We're going to erase {filename}."
print("If you don't want that, hit CTLR-C (^C).")
print("If you don't want that hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')#making a variable target to select the target file

print("Truncating the file. Goodbye!")
target.truncate()#truncate (deletes) the target(selection for the file)

print("Now am going to ask you for three lines.")

line1 = input("line 1: ")#this is to add
line2 = input("line 2: ")#the three lines
line3 = input("line 3: ")#from the keyboard

print("I'm going to write these to the file.")

target.write(line1)#this writes the line1 variable on the file
target.write("\n")#this tells python to start on a newline
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()#this closes the variable target which is for selecting the file
