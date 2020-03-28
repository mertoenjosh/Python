def power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return(result)

# can you make the output be thi power that is answer
print("The answer is "+str((power(int(input("Enter base number:\n> ")), int(input("Enter power number:\n> "))))))
#print("The answer is {}".format(answer))
