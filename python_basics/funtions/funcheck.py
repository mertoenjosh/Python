print("""The following are tips for
    \t:creating a function""")

def creating_function(*args):
    tip1, tip2, tip3, tip4, tip5, tip6, tip7, tip8 = args
    print("Tip 1: {}".format(tip1))
    print("Tip 2: {}".format(tip2))
    print("Tip 3: {}".format(tip3))
    print("Tip 4: {}".format(tip4))
    print("Tip 5: {}".format(tip5))
    print("Tip 6: {}".format(tip6))
    print("Tip 7: {}".format(tip7))
    print("Tip 8: {}".format(tip8))

def calling_function(tip1, tip2, tip3, tip4):
     print("Tip 1: {}".format(tip1))
     print("Tip 2: {}".format(tip2))
     print("Tip 3: {}".format(tip3))
     print("Tip 4: {}".format(tip4))

creating_function(
    "Function must sart with 'def'.",
    "Should have only characters and underscore.",
    "Put an opening bracket after function name.",
    "Put argument after parenthesis and separate them with commas(,).",
    "Arguments should be unique.",
    "Put a closing bracket and the a colon.",
    "Use four spaces indents(one tab space) to indent lines of code you want the function.",
    "End your function by dedenting. Going back to writing with no indent."
)
print("\t:calling a functon")
calling_function(
    "Call it by typing it's name.",
    "Put the '(' character after the name.",
    "Put values for argument and separate the with commas if they are many.",
    "End function call with a ')' character."
)
