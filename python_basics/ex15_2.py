from sys import argv
script = argv
print("Type file name:")
file = input('> ')
x = open(file)
print(x.read())
x.close()
