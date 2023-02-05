import random
  

def validPlay(userInput):
    """Returns user input if it exists in rpsOptions List, otherwise displays error message with new prompt."""

    attemptCount = 0
    while True:
        attemptCount += 1
        try:
            rpsOptions.index(userInput)  # Checks if input exists in List.
            return userInput
        except:
            if attemptCount < 5: userInput = input("\nThat's not a valid play, but don't worry :)\n\nJust try again: ")
            # Error message changes after 4th invalid attempt.
            else: userInput = input("\nThat's still not a valid play :(\n\nPlease try again: ")


rpsOptions = ["rock", "paper", "scissors"]

# Dictionary with user winning options and their descriptions (First eg. Rock smashes Scissors).
userWin = {"rockscissors" : "smashes", "paperrock" : "covers", "scissorspaper" : "cuts"}

# User losing options.
userLose = {"scissorsrock" : "smashes", "rockpaper" : "covers", "paperscissors" : "cuts"}

print("""\n\n------------  Want to play Rock Paper Scissors?  ------------
------------         Let the game begin!         ------------""")

while True:
    userMove = validPlay(input("\n\nMake your move: ").lower())  # Checks validity of input.
    gameMove = random.choice(rpsOptions)  # Stores a randomly selected RPS option from List.

    if gameMove == userMove:
        print(f"\n{userMove.title()} vs. {gameMove.title()} - It's a tie!")
    else:
        comparison = userMove + gameMove  # Concatenates as single str value.

        if comparison in userWin:
            # If value exists as a key in userWin Dict, prints winning message with description.
            print(f"\nYou win! {userMove.title()} {userWin[comparison]} {gameMove.title()}!")
        elif comparison in userLose:
            # If value exists as a key in userLose Dict, prints losing message with description.
            print(f"\nYou lose! {gameMove.title()} {userLose[comparison]} {userMove.title()}!")

    gameLoop = input("\n\nWould you like to play again?\nPlease type 'Y' for Yes or 'N' for No: ").upper()

    # Keeps looping until user input is either 'Y' or 'N'.
    while gameLoop not in ['Y', 'N']: gameLoop = input("\nPlease only enter 'Y' or 'N': ").upper()
        
    # Ends program if user input is 'N'.
    if gameLoop == 'N':
        print("\n\nThank you for playing Rock Paper Scissors :)\nGame has ended.\n")
        break