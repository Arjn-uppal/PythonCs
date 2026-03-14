inputPath = "SuitsAndValues.txt"

def ReadDeckFromFile():
    

    #Open the file for reading
    file = open(inputPath, "r")

    #This is an empty list to store the data
    cardList = []

    #Reads each line in the text file and adds each line to a list and
    #adds the list to a 2D list
    for i in range(0, 2):
        cardInfoRow = []
        entries = file.readline().rstrip("\n")
        cardInfoRow.append(entries)
        cardList.append(cardInfoRow)

    #File is completely read so close it
    file.close()

    print("")

    #This makes each entry in each row be it's own string so we can individualy access them later
    cardList = [cardInfoRow[0].split(',') for cardInfoRow in cardList]

    #This is the list of all the cards
    cardPairList = []

    #This allows the list to have multiple rows
    for y in range(0, len(cardList[0])):

        #A row that contains a constant letter with changing numbers
        suitValPair = []

        #This allows the list to have multiple columns
        for x in range(0, len(cardList[1])):

            #First term represents the shift in values
            #Second term represents the shift in suits
            card = cardList[1][x] + cardList[0][y]
            suitValPair.append(card)
        
        #print(suitValPair)

        #This adds each row to the list
        cardPairList.append(suitValPair)

    #print("")
    #returns the list of cards
    return cardPairList

def AskUserCard():
    #Asks User for input and returns it
    cardRemoval = input("What card do you want to remove: ")
    return cardRemoval

def OutputDeck(deck, cardToRemove):    
    #Print out deck in the given format
    #print(cardPairList)

    #The boolean variable allows the program to tell if the specified card 
    #to remove is in the list and if it is not
    cardFound = False
    
    #Searches through the entire 2D list of cards and compares the
    #users input to each entry. Then it returns the modified 2D list
    #depending on what the user input was
    for suit in range(0, len(deck)):
        for card in range(0, len(deck[suit])):

            #If the specified card is found, replace it with a dash symbol
            if deck[suit][card] == cardToRemove:            
                deck[suit][card] = "—"
                cardFound = True            
    
    #If something else was inputed that was not a card with the exception
    #of a blank input, print the following message
    if cardToRemove !="" and cardFound == False:
        print("Your card is not in the deck.")
    else:
        #Write out the modified deck
        for suit in range(0, len(deck)):
            for card in range(0, len(deck[suit])):
                print(deck[suit][card], end=" ")
            print()

    return deck

def main():
    #deck is now the flexible 2D card list
    deck = ReadDeckFromFile()

    #This is what prints the full deck of cards before any are removed.
    #The second blank parameter is utilized later to make a decision
    deck = OutputDeck(deck, "")
    print()

    #The code will loop forever asking the user to remove cards until
    #a blank input for the removal of a card is entered
    while True:
        card = AskUserCard()

        #This changes the 2D list to the returned value and utilizes the
        #users input as a parameter
        deck = OutputDeck(deck, card)
        print()

        #If the users input for which card to remove was a blank statement, stop the program
        if card == "":
            break

main()
