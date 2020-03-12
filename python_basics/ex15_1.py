#solution for strings...type a string with its quotes
#    at the konsole..huu haa
from sys import argv

script = argv

#txt = open(filename)

#print("Here's your file {}:".format(filename))
#after openning now you are telling python to read fron the specified filename
#print(txt.read())

print("Type the file name :")
file = input('> ')

txt = open(file)

print(txt.read())
file = input('close y 0r n: ')
txt.close()
