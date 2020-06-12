number = 0
#limit=True
while True:
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)
    number+=1
