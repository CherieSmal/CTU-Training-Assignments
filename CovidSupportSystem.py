def testargs(userInput, inputParam, errorMsg = "Invalid input. Try again"):
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
    The second argument must be a List format containing string or integer values which are the accepted values.
    The List can contain a single value, multiple values, or a range of values.

    errorMsg (str):
    An optional customizable string error message that is returned if conditions aren't met.
    The third argument is an optional error message which could be customized.
    

    RETURNS
    userInput (str):
    Returns the input in string format if it meets the specified conditions.

    errorMsg (str):
    A string error message keeps returning if the conditions aren't met, and user is prompted for correct input.
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



mainMenu = ("""

***********************************************************************
Welcome to the COVID-19 support service. Please select an option below:
1. Statistics
2. Prevention
3. Symptoms
4. Treatment
5. Report case
6. Exit
Please enter a number from 1 to 6: """)

# Options from 'mainMenu' list declared as variables for better readability.
statistics = '1'
prevention = '2'
symptoms = '3'
treatment = '4'
reportCase = '5'
exit = '6'

# 'Treatment' message declared as variable for multiple calling.
treatmentMsg = """
If you feel sick, you should:

>>> Rest
>>> Drink a lot of fluids
>>> Eat nutritious food
>>> Stay in a separate room from other family members.
>>> Use a dedicated bathroom if possible.
>>> Clean and disinfect frequently-touched surfaces."""

# List to store updated Covid cases count.
# SA, USA and China are last in the List so that they're not displayed when user selects a number from 0 - 9 for random country (line 39).
countryList =[
        ["Russia", 290603], ["India", 134933], ["Belgium", 142419], ["Hong Kong", 134896], ["Singapore", 90514], ["Chile", 46298],
        ["Israel", 36440], ["Australia", 7155], ["Qatar", 6270], ["Uruguay", 1768], ["SA", 27403], ["USA", 1700000], ["China", 82995]
        ]

listNum = ""

# Program loops until 'exit' is selected by user.
while listNum != exit:

    # Function checks that user input is a valid number between 1 and 6, otherwise an error msg will occur.
    listNum = testargs(input(mainMenu), list(range(1, 6 + 1)), "\nInput is not valid. Please enter a choice of 1, 2, 3, 4, 5, or 6: ")

    # If 'statistics' is selected by the user, print the List index values for SA, USA and China.
    if listNum == statistics:
        print(f"""\n
Currently in SA there are {countryList[10][1]} confirmed cases.
Currently in USA there are {countryList[11][1]} confirmed cases.
Currently in China there are {countryList[12][1]} confirmed cases.""")

        randomCase = testargs(input("\nWould you like to see the confirmed cases for a random country? Y/N: "), \
        ['Y', 'N'], "\nPlease only insert the letters 'Y' for Yes or 'N' for No: ")

        if randomCase == 'Y':
            randomCountry = testargs(input("\nTo select a random country, type a number from 0 to 9: "), \
            list(range(0, 9 + 1)), "\nTo select a random country, please only type a number from 0 to 9: ")

            # If user selects to see a random country's cases and they pick a number, the values of that index in the List prints.
            print(f"\n>>> {countryList[int(randomCountry)][0]} has {countryList[int(randomCountry)][1]} confirmed cases.")

    elif listNum == prevention:
        print("""\n
To prevent the spread of COVID-19:

>>> Clean your hands often. Use soap and water, or an alcohol-based hand rub.
>>> Maintain a safe distance from anyone who is coughing or sneezing.
>>> Don't touch your eyes, nose or mouth.
>>> Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.
>>> Stay home if you feel unwell.
>>> If you have a fever, cough and difficulty breathing, seek medical attention. Call in advance.
>>> Follow the directions of your local heath authority.""")

    elif listNum == symptoms:
        print("""\n
>>> Most Common Symptoms:
    Fever
    Dry cough
    Tiredness

>>> Less Common Symptoms:
    Aches and pains
    Sore throat
    Diarrhea
    Conjunctivitis
    Headache
    Loss of taste or smell
    A rash on skin, or discolouration of fingers or toes.

>>> Serious Symptoms:
    Difficulty breathing or shortness of breath
    Chest pain or pressure
    Loss of speech or movement""")

    elif listNum == treatment:
        print(f"\n{treatmentMsg}")

    elif listNum == reportCase:
        haveSymptom = testargs(input("""\n
Do you have any of the symptoms? Y/N: """), ['Y', 'N'], \
"\nPlease only insert the letters 'Y' for Yes or 'N' for No: ")
        
        if haveSymptom == 'Y':
            hasCovid = testargs(input("\nIs your temperature above 38.5°C? Y/N: "), ['Y', 'N'], \
"\nPlease only insert the letters 'Y' for Yes or 'N' for No: """)

            if hasCovid == 'Y':
                caseCountry = testargs(input("""
In which country are you? Select an option below:
1. SA
2. USA
3. China
Enter choice from 1 to 3: """), [1, 2, 3], "\nPlease only enter a choice of 1, 2 or 3: ")
                
                # If user has Covid, their selected country's confirmed cases increase by one in the List.
                # In other words, the 'countryList' index value of that specific country increments by one.
                if caseCountry == '1': countryList[10][1] = countryList[10][1] + 1
                elif caseCountry == '2': countryList[11][1] = countryList[11][1] + 1
                elif caseCountry == '3': countryList [12][1] = countryList[12][1] + 1

                print('\033[1;1m' + "\n\nYou have COVID-19 :(" + '\033[0m')  # Prints message in bold.
                print(treatmentMsg)
            else:
                print('\033[1;1m' + """\n
Hooray! You do not have COVID-19! :)""" + '\033[0m')

        else:
            print('\033[1;1m' + """\n
Hooray! You do not have COVID-19! :)""" + '\033[0m')

# The below msg prints if the user selects 'exit'.
print("\nThank you for visiting the Covid Support System. Check in again soon! :)")
print('\033[1;3m' + "(This program has closed)\n" + '\033[0m')  # Prints message in bold and italics.