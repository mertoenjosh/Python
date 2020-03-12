#this script works with intergers only
#read about declaring strings
from sys import argv

script, user_name = argv
prompt = '> '

print("Hi {}".format(user_name), "I'm the {}".format(script), "script.")
print("I'd like to ask you a few questions.")
print("Do you like me {}?").format(user_name)
likes = (input(prompt))

print("Where do you live {}?").format(user_name)
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print('''Alright, so you said {}'''.format(likes), '''about liking me. You live in {}'''.format(lives),'''. Not sure where that is. And you have a {}'''.format(computer),'''computer. Nice.''')
