import random

def Coin_Flip():
    #coin
    cSide = random.randint(0, 1)

    coinResult = ""

    #Heads when flipped
    if cSide == 0:
        coinResult = "Win"
        return coinResult
        
    else:
        coinResult = "Lose"
        return coinResult
        
    
def First_Dice_Roll():
    #First Dice
    diceSide = random.randint(1, 6)
    ratio = diceSide / 2

    fstDiceResult = ""

    #Even when rolled
    if ratio % 2 == 0:
        fstDiceResult = "Win"
        return fstDiceResult
    else:
        fstDiceResult = "Lose"
        return fstDiceResult


def Second_Dice_Roll():
    #Second Dice
    diceSide = random.randint(1, 6)
    ratio = diceSide / 2

    secDiceResult = ""

    #Odd when rolled
    if ratio % 2 == 1:
        secDiceResult = "Win"
        return secDiceResult
    else:
        secDiceResult = "Lose"
        return secDiceResult


def Third_Dice_Roll():
    #Third Dice
    diceSide = random.randint(1, 6)

    thrdDiceResult = ""

    #Between 2 - 4 when rolled
    if diceSide == 2 or 3 or 4:
        thrdDiceResult = "Win"
        return thrdDiceResult
    else:
        thrdDiceResult = "Lose"
        return thrdDiceResult


def Calc_Exp_Prob(gamesPlayed, numWins):
    #Calculates the experimental probability
    exProb = numWins / gamesPlayed
    return exProb

def main():
    #Determines the number of games that will be played
    gamesPlayed = random.randint(100, 1000)
    
    print("")
    print("Games played:", gamesPlayed)
    print("")

    #You start with zero wins
    numWins = 0

    #Necessary loop for playing the game multiple times
    x = 0 # loop control
    while x <= gamesPlayed:
        cF = Coin_Flip()

        fD = First_Dice_Roll()

        sD = Second_Dice_Roll()

        thD = Third_Dice_Roll()

        #Determines if you won or not and updates the number of games won
        if cF == "Win" and fD == "Win" and sD == "Win" and thD == "Win":
            numWins += 1

        #This prevents the program from playing the game infinitly
        x += 1
    
    print("Games won:", numWins)
    print("")

    experimentalProb = Calc_Exp_Prob(gamesPlayed, numWins)

    #Displays final result as a percentage
    print(f"The experimental probability of winning is {experimentalProb:.2%}")

    
main()