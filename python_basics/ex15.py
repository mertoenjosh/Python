from sys import argv

script, filename = argv

txt = open(filename)#this is to open the file you named on argv
print(f"Here's your file {filename}:")
#after openning now you are telling python to read fron the specified filename
print(txt.read())

print("Type the file name again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
