#this script is supporsed to copy file to another..python3
from sys import argv
#we've imported another module
from os.path import exists
#created 3 variables of which two youll write the files
script, from_file, to_file = argv
#the formats calls for the specified files during launch
print("Copying from {}".format(from_file), "to {}".format(to_file))

#creating another variables
in_file = open(from_file)#this variable is selecting the file from_file
indata = in_file.read()#this variable is reading the selected file
#the len on format is to fetch length of the file
print("The input file is".format(len(indata)), "bytes long")
#my format did not return true or false,, try it on python3
print("Does the output file exist?".format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
