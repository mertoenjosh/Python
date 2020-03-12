def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}".format(arg1), "arg2: {}".format(arg2))

def print_two_again(arg1, arg2):
    print("arg1: {}".format(arg1), "arg2: {}".format(arg2))

def print_one(arg1):
    print("arg1: {}".format(arg1))

def print_none():
    print("I got no argument")

print_two("Martin", "Thuo")
print_two_again("Martin", "Thuo")
print_one("First!!")
print_none()
