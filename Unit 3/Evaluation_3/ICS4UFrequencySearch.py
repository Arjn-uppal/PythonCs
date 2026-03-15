inputPath = "IntegerData.txt"

# Finds the frequent integer that corresponds to the user's input
def FindNthMostFrequent(userFrequency, integerList):

    # Bubble sort algorithm that sorts the integer list in ascending order.
    # The number of "Bubble Cycles" is the length of the list
    for i in range(0, len(integerList)):

        # Cycle through all adjacent elements not yet sorted (reduces each time)
        for  j in range(1, len(integerList) - i):
            
            # Check for out of order and swap elements
            if integerList[j - 1] > integerList[j]:

                swapValue = integerList[j]
                integerList[j] = integerList[j - 1]
                integerList[j - 1] = swapValue

    # The code below is the strategy because you would end up with an 
    # infinite amount of if statements checking for each frequency level

    # Make a list of unique values by removing repeating values in the sorted integer list
    uniqueVals = []

    for index in range(0, len(integerList)):

        uniqueVals.append(integerList[index])

        if integerList[index] == integerList[index - 1]:
            uniqueVals.remove(integerList[index])
        
    # Make a list of frequencies that correspond 
    # to each unique value in the unique value list
    frequencyList = []

    for uniqueValIndex in range(0, len(uniqueVals)):

        frequency = 0

        for integerListIndex in range(0, len(integerList)):

            if uniqueVals[uniqueValIndex] == integerList[integerListIndex]:
                frequency += 1

        frequencyList.append(frequency)

    return frequencyList
    n = 1
    #while n <= frequencyLevel:


# Reads the integer data file
def ReadIntsFromFile(inputPath):

    # List that stores values from the data file
    integerList = []

    integerFile = open(inputPath, "r")

    # Reads each line, converts string to int, and adds it to a list.
    # Stops reading the file when it gets to the end
    while True:
        singularInteger = integerFile.readline().rstrip("\n")

        if singularInteger == "":
            break
        else:
            trueInt = int(singularInteger)
            integerList.append(trueInt)

    # File is completely read so close it
    integerFile.close()
    
    return integerList


# Ask the user for their input
def AskUserFrequency():

    # input for finding frequent values in the list
    frequencyLevel = int(input("Pick an integer frequency level: "))
    
    return frequencyLevel

 
# Reads the integer file and allows user to pick Nth most frequent
def main():

    integerList = ReadIntsFromFile(inputPath)
    userFrequency = AskUserFrequency()
    nthMostFrequentValue = FindNthMostFrequent(userFrequency, integerList)
    # ReportUserFrequencyValue(nthMostFrequentValue, userFrequency)

    occuringInteger = FindNthMostFrequent(userFrequency, integerList)

    print()
    print(occuringInteger)

main()