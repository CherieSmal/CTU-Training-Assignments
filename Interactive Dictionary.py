import json


def inputtest(userInput):
    """Returns user input, else displays error message and prompts user for new input if it does not meet requirements."""

    userInput = userInput.upper()
    
    while userInput not in ["Y", "N"]:
        userInput = input("\nPlease enter 'Y' for Yes or 'N' for No: ").upper()
    return userInput


dictionary = {
    "different" : "Not the same as another or each other; unlike in nature, form, or quality.",
    "kind" : "A group of people or things having similar characteristics.",
    "consciousness" : "The state of being aware of and responsive to one's surroundings.",
    "appreciation" : "Recognition and enjoyment of the good qualities of someone or something.",
    "sustainable" : "Able to be maintained at a certain rate or level.",
    "dominant" : "Having power and influence over others.",
    "flexibility" : "The quality of bending easily without breaking.",
    "gaslight" : "Manipulate (someone) by psychological means into doubting their own sanity.",
    "humour" : "The quality of being amusing or comic, especially as expressed in literature or speech.",
    "jargon" : "Special words or expressions used by a profession or group that are difficult for others to understand.",
    "love" : "An intense feeling of deep affection.",
    "banter" : "The playful and friendly exchange of teasing remarks.",
    "violence" : "Behaviour involving physical force intended to hurt, damage, or kill someone or something.",
    "mystery" : "Something that is difficult or impossible to understand or explain.",
    "naughty" : "(Especially of a child) badly behaved; disobedient.",
    "recycle" : "Convert (waste) into reusable material.",
    "possibility" : "A thing that may happen or be the case.",
    "talent" : "Natural aptitude or skill.",
    "expert" : "A person who is very knowledgeable about or skilful in a particular area.",
    "intangible" : "Unable to be touched; not having physical presence."
    }

# Creates a json file and writes the dictionary contents to the file.
jsonFile = json.dumps(dictionary)
with open( "dictFile.json", "w" ) as fileObj:
    fileObj.write(jsonFile)

print("""
_______________________________________

Welcome to your Interactive Dictionary!
_______________________________________
""")

count = 0
matchDict = {}

# Main program loop.
while True:
    searchWord = input("\nEnter the word you want to search: ").lower()

    # Opens the json file to read the data and search for the user input word.
    # Prints word and definition if word exists in Dictionary.
    try:
        with open("dictFile.json", "r") as fileObj:
            openDict = fileObj.read()
            openDict.find(searchWord)
            openDict = json.loads(openDict)  # Formats file data as type Dict.
            print(f"\n\n{searchWord.title()}\n{openDict[searchWord]}\n")
            
    # If user's exact search word does not exist in Dictionary.
    except:
        print("Sorry, word not found :(")

        # Increments count of matching characters in Dict key words and user search words.
        for key in openDict:
            for char, index in zip(key, searchWord):
                if char == index: count += 1

            # If specified matches are found, appends keys with their values to matchDict.
            if len(searchWord) < 4 and count > 1:
                matchDict[key] = openDict[key]
            elif len(searchWord) > 3 and len(searchWord) < 7 and count > 2:
                matchDict[key] = openDict[key]
            elif len(searchWord) > 6 and count > 4:
                matchDict[key] = openDict[key]

            count = 0  # Resets count for a new word match search.
        
        # If match/es found, gives user option to view match results.
        if len(matchDict) > 0:
            closeMatch = inputtest(input("\nDo you want to find a close match? Enter 'Y' for Yes or 'N' for No: "))
            if closeMatch == "Y":
                for key in matchDict: print(f"\n\n{key.title()}\n{matchDict[key]}\n")
            else:
                break  # Ends program.
    
    newSearch = inputtest(input("\nDo you want to search another word? Enter 'Y' for Yes or 'N' for No: "))

    # Clears matches in matchDict for new word match search.
    # Else ends program.
    if newSearch == "Y": matchDict.clear()
    else: break

print("\n\nThank you for using your Interactive Dictionary.\nThe program has ended :)\n")