def CreateListOfCases():
    #List of prize values in the game
    return [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

def CaseAverage(prizeValList):
    #Calculating the average of all the prize values of the unopened cases
    averagePrizeVal = sum(prizeValList) / len(prizeValList)
    return averagePrizeVal

def AskPlayerChooseCases():
    #Player is choosing what cases they want to pick from the 10 cases
    while True:
        playerChooseCases = input("Choose case numbers (integers) to remove from 1 to 10:")
        #This determines if program stops or not
        if playerChooseCases == "":
            return "break"
        else:
            #Convert string to array of ints
            #We need to sort the array because later we walk it backards removing cases by array index
            caseArray = playerChooseCases.split(",")
            if all(item.isdigit() for item in caseArray):
                caseArrayInts = [int(item) for item in caseArray]   
                if all(0 < x <= 10 for x in caseArrayInts):
                    caseArrayInts.sort()
                    return caseArrayInts

def BankerOffer():
     #Input from the banker
     bankerOfferVal = getInt("Enter banker's offer:")
     return bankerOfferVal

def RemainingCases(prizeValList, playerChooseCases):
        #This makes a new list of remaining cases by excluding the cases that the user chose.
        #This is a necessary step for calculating the average of the remaining unopened cases
        for i in range(len(playerChooseCases)-1, -1, -1):
            prizeValList.remove(prizeValList[playerChooseCases[i] - 1])
        return prizeValList

def AcceptingDealOrNot(OfferOfBanker, newAverage):
     #Comparing the banker's offer to the average of the remaining unopened cases and making a recommendation to the player
     if OfferOfBanker > newAverage:
          print("The player should take the deal")
     else:
          print("The player should not take the deal")

def getInt(prompt):
    #Ask for an integer and validate before returning
    while True:
        inputString = input(prompt)
        if inputString.isdigit():
            return int(inputString)
        
#This main method calls all the other methods in the program
def main():
    print("")

    #This lets the player continue the simulation until they enter a blank input of cases
    while True:
        #This creates the original list of cases
        cases = CreateListOfCases()
        print("Cases:", cases)

        playerCases = AskPlayerChooseCases()
        print("")

        #The code that gets executed from here on out depends on the returned input value of cases chosen
        if playerCases == "break":
             break
        else:
            print("Player cases:", playerCases)

            OfferOfBanker = BankerOffer()
            print("")

            casesRemaining = RemainingCases(cases, playerCases)
            print("Cases Remaining:", casesRemaining)

            newAverage = CaseAverage(casesRemaining)
            print("Average of remaining unopened cases: $", round(newAverage, 2), sep='')
            print("")

            AcceptingDealOrNot(OfferOfBanker, newAverage)
            print("")

main()