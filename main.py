print("Game of threes")

validInput = False
while validInput == False:
    inputString = input("Please enter a number:\n> ")
    try:
        number = int(inputString)
        validInput = True
    except:
        print("Invalid input, try again")

print("Starting with " + str(number))
while number > 1:
    if number % 3 == 0:
        number /= 3
        print(str(number * 3) + " divided by 3 equals " + str(number))
    elif (number + 1) % 3 == 0:
        number = (number + 1) / 3
        print(str(number * 3 - 1) + " plus 1 then divided by 3 equals " + str(number))
    else:
        number = (number - 1) / 3
        print(str(number * 3 + 1) + " minus 1 then divided by 3 equals " + str(number))

print("Done!")
