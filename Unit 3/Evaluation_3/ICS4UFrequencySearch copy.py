inputPath = "IntegerData2.txt"

#Binary Search modified to search the first "column" of a 2-d array of arrays
#a is the list to search through
#target is the value being searched for
#Returns the index of the last occurence of target
#Returns -1 if the target is not found
def binarySearch(a, target):

	#Look at the list between first and last index values
	first = 0
	last = len(a) - 1

	while first <= last:

		#Middle of the current portion being looked at (index must be int)
		mid = (first + last) // 2

		#Discard right half by setting new last
		if target < a[mid][0]:
			last = mid - 1

		#Discard left half by setting new first
		elif target > a[mid][0]:
			first = mid + 1

		#Found target
		else:
			return mid

	#Only gets here if target wasn't found
	return -1


def quickSort(a):
	sortPartition(a,0,len(a)-1)

def sortPartition(a,low,high):

	if low < high:

		#Set Markers
		left = low
		right = high

		#Pick Pivot
		pivot = a[low]

		#Set Active Marker
		active = "R"

		#Partition the list
		while left < right:

			#Right marker action
			if active == "R":

				#Move right marker left until it finds a value on the wrong side
				while a[right] >= pivot and left < right:
					right = right - 1

				#Move value that is on the wrong side
				a[left] = a[right]

				#Make other side active
				active = "L"


			if active == "L":

				#Move left marker until it finds a value on the wrong side
				while a[left] <= pivot and left < right:
					left = left + 1

				#Move value that is on the wrong side
				a[right] = a[left]

				#Make other side active
				active = "R"

		#Put pivot in the correct position
		a[left] = pivot

		#Recursive sort the left partition
		sortPartition(a,low,left-1)

		#Recursive sort the right partition
		sortPartition(a,right + 1, high)


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

#count through the integer list making a 2d list of unique values and frequencies
def TallyUpIntegers(integerList):

    #First sort the list, so that we can use binary search on it
    quickSort(integerList)

    frequencies = []
    #Walk the integer list, maintaining a count of each occurrence
    for intIndex in range(0, len(integerList)):
        singleDataValue = integerList[intIndex]
        #Search the frequencies list for the single data value
        foundIndex = binarySearch(frequencies, singleDataValue)
        if foundIndex > -1:
            #If data value is found, then increment the frequency by 1
            foundFrequency = frequencies[foundIndex]
            foundFrequency[1] += 1
        else:
            #Data value is not found, so add a new "row" for it with starting frequence of 1 
            frequencies.append([singleDataValue, 1])        

    return frequencies

    


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

    #userFrequency = AskUserFrequency()

    countedIntList = TallyUpIntegers(integerList)
    print (countedIntList)
    #countedIntList = twoDList(integerList)

    #nthMostFrequentValue = FindNthMostFrequent(userFrequency, integerList)
    # ReportUserFrequencyValue(nthMostFrequentValue, userFrequency)

    #occuringInteger = FindNthMostFrequent(userFrequency, integerList)

    #print()
    #print(countedIntList)
    

main()