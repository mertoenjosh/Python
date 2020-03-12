i = 0
numbers = []

def whilefunc(callfunc):
    print("The numbers: ")

    while i < 6:
        print(f"At the top is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

whilefunc("Printing")

for num in numbers:
    print(num)
