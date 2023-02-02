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


# List contains all the bonus amounts.
bonusPayout = [
    [5.00, 9.00, 16.00, 22.00, 30.00],
    [10.00, 12.00, 18.00, 24.00, 36.00],
    [20.00, 25.00, 32.00, 42.00, 53.00],
    [32.00, 38.00, 45.00, 55.00, 68.00],
    [46.00, 54.00, 65.00, 77.00, 90.00],
    [60.00, 72.00, 84.00, 96.00, 120.00],
    [85.00, 100.00, 120.00, 140.00, 175.00],
]

# Main program loop.
while True:
    print("""\n--------------------------------
--------------------------------\n
Welcome to your Bonus Calculator
\n--------------------------------
--------------------------------\n""")

    print("\nPlease enter '999' to end program, or \nenter the number of full weeks worked:")

    # Function checks that user input is a valid number between 0 and 999, otherwise an error msg will occur.
    fullWorkWeeks = testinput(input("\n>>> "), list(range(0, 999 + 1)), \
    "\nInput is not recognized.\nPlease enter the number of full weeks worked.\n\n>>> ")

    # Program ends if '999' is input.
    if fullWorkWeeks == '999': break

    print("\nPlease enter the number of positive reviews received:")
    goodReviews = input("\n>>> ")

    # Error handling While loop - user can only input a whole number.
    while int(goodReviews.isnumeric()) == False: goodReviews = input("""\nInput is not recognized.
Please enter the number of positive reviews received.\n\n>>> """)

    # If user inputs are numbers greater than 6 and 4,
    # '6' and '4' are stored in the variables so that input stays within the bonusPayout List index range.
    # They are stored as strings for conistency in the code.
    if int(fullWorkWeeks) > 6: fullWorkWeeks = '6'
    if int(goodReviews) > 4: goodReviews = '4'

    # Prints the amount from bonusPayout List, called by the user input.
    print(f"""
The bonus payout is:
$ {"%.2f" % bonusPayout[int(fullWorkWeeks)][int(goodReviews)]}
""")

print('\033[1;3m' + "\n(This program has ended)\n" + '\033[0m')