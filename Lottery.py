import random


def testinput(userInput, inputParam, errorMsg = "Invalid input. Try again"):
    """
    An error handling function that returns input if it meets the argument specifications.

    Example 1 (int):
    testinput(input("Enter a number from 1 - 9: "), list(range(1, 9 + 1)), "Invalid input!")

    Example 2 (str):
    testinput(input("Enter y for Yes or n for No: "), ["y", "n"], "Invalid input!")
    
    
    PARAMETERS
    userInput (str or int):
    The input argument, which can be a string or integer, that needs to be checked.

    inputParam (list):
    The second argument must be a list format containing string or integer values which are the accepted values.
    The list can contain a single value, multiple values, or a range of values.

    errorMsg (str):
    An optional customizable string error message that will be returned if conditions aren't met.
    The third argument is an optional error message which could be customized.
    

    RETURNS
    userInput (str):
    Returns the input in string format if it meets the specified conditions.

    errorMsg (str):
    A string error message that will keep returning if the conditions aren't met.
    """
    while True:
        if type(inputParam[0]) == int:
            try:
                uInput = int(userInput)
                if uInput in inputParam: return userInput
                else: raise ValueError
            except:
                userInput = input(errorMsg)

        elif type(inputParam[0]) == str:
            if inputParam[0] == inputParam[0].upper():
                userInput = userInput.upper()
            elif inputParam[0] == inputParam[0].lower():
                userInput = userInput.lower()

            if userInput in inputParam: return userInput
            else: userInput = input(errorMsg)


play = "Y"

while play != "N":
    randomNumbers = []

    # Value determines the amount of guess and random numbers.
    lotteryNum = 3

    # Lottery random generated numbers.
    for number in range(lotteryNum): randomNumbers.append(random.randint(0, 9))

    print("""\n
********************************************************************************

Welcome to the Lottery!
You will be asked to guess 3 numbers; for each guess, pick a number from 0 to 9.
The better the match, the better the prize:
1 match - $10
2 matches - $100
3 random matches - $1,000
3 exact matches - $1,000,000
No matches - No prize

Goodluck!

********************************************************************************
""")

    guessList = []
    guessNum = 0

    for guess in range(lotteryNum):
        guessNum += 1

        # Function checks that user input is a valid number between 0 and 9, otherwise an error msg will occur.
        userGuess = testinput(input(f"""\nPlease enter guess number {guessNum}. \nYour input: """), \
        list(range(0, 9 + 1)), "\nRemember to pick a number only from 0 to 9: ")

        # Converts the user input to int for easier matching againts random numbers later on in code.
        userGuess = int(userGuess)
        guessList.append(userGuess)

    print(f"\n\nThe lucky numbers are: {randomNumbers[0]} {randomNumbers[1]} {randomNumbers[2]}")
    print(f"\nYour 3 guesses are: {guessList[0]} {guessList[1]} {guessList[2]}")

    # Stores the user guesses as str to easily compare to random numbers for exact match.
    userGuessList = str(guessList)

    matchCount = 0

    # Loops through the 3 random generated numbers, and user guessed numbers;
    # if there is a match, updates matched guess number to 10 - will never match again.
    # This avoids unwanted duplicate matches.
    for index in range(len(randomNumbers)):
        for number in range(len(guessList)):
            if randomNumbers[index] == guessList[number]:
                matchCount +=1
                guessList[number] = 10
                break

    # Converts the random numbers to str, to easily compare to guessed numbers for exact match.
    randomNumbers = str(randomNumbers)

    # If the random numbers are exactly the same as the guessed numbers, award is $1,000,000.
    if randomNumbers == userGuessList:
        awardAmt = "$1,000,000"
        # Converts match count to str for better printout later on.
        matchCount = str("3 exact")
    elif matchCount == 3:
        awardAmt = "$1,000"
    elif matchCount == 2:
        awardAmt = "$100"
    elif matchCount == 1:
        awardAmt = "$10"
    else:
        awardAmt = "$0"

    # Prints how many matches there are, and the award amount.
    if matchCount == 1:print(f"\nYou have {matchCount} match!\nYou have won: {awardAmt}")
    else: print(f"\nYou have {matchCount} matches!\nYou have won: {awardAmt}")

    # Gives user the option to play again.
    play = testinput(input("""\n\nWould you like to play again? 
Please enter 'Y' for Yes or 'N' for No: """), ["Y", "N"], "\nPlease only enter 'Y' for Yes or 'N' for No: ")

# End of program message.
print("""

Thank you for taking part in the Lottery.
Check in again soon! :)
""")