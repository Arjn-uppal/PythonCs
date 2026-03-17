import sys

inputPath = "Unit 3/Evaluation_3/InputFiles/Q1 102 Two Frequencies.txt"

# TESTED with input files up to 20,000 lines. Larger may cause recursion limit error.
# Recursion limit is set to 8000 
sys.setrecursionlimit(8000)


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

# Imported from class notes
def quickSort(a):
	sortPartition(a,0,len(a)-1)

# Imported from class notes
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

#Quick Sort adapted to sort a 2D list based on the chosen element of each "row" array
#Used for sorting the frequency table
def quickSort2D(a, sortColumnIndex):
	sortPartition2D(a,0,len(a)-1, sortColumnIndex)

#Recursive part of Quick Sort adapted to 2D lists      
def sortPartition2D(a,low,high, sortColumnIndex):

	if low < high:

		#Set Markers
		left = low
		right = high

		#Pick Pivot
		pivot = a[low][sortColumnIndex]
		pivotRow = a[low]
		
		#Set Active Marker
		active = "R"

		#Partition the list
		while left < right:

			#Right marker action
			if active == "R":

				#Move right marker left until it finds a value on the wrong side
				while a[right][sortColumnIndex] >= pivot and left < right:
					right = right - 1

				#Move value that is on the wrong side
				a[left] = a[right]

				#Make other side active
				active = "L"


			if active == "L":

				#Move left marker until it finds a value on the wrong side
				while a[left][sortColumnIndex] <= pivot and left < right:
					left = left + 1

				#Move value that is on the wrong side
				a[right] = a[left]

				#Make other side active
				active = "R"

		#Put pivot in the correct position
		a[left] = pivotRow

		#Recursive sort the left partition
		sortPartition2D(a,low,left-1, sortColumnIndex)

		#Recursive sort the right partition
		sortPartition2D(a,right + 1, high, sortColumnIndex)
		

#count through the integer list making a 2d list of unique values and frequencies
def TallyUpIntegers(integerList):

	#First sort the list, so that the new list we make is made in order, so we can use binary search on it
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

# Make sure the string holds an integer
def represents_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False


# Reads the integer data file
def ReadIntsFromFile(inputPath):

	# List that stores values from the data file
	integerList = []

	try:
		integerFile = open(inputPath, "r")
	except Exception as e:
		print(f"An error occurred: {e}") 
		return integerList

	
	# Reads all lines, converts string to int, and adds it to a list.
	for line in integerFile:
		singularInteger = line.rstrip("\n")

		if represents_int(singularInteger):
			trueInt = int(singularInteger)
			integerList.append(trueInt)

	# File is completely read so close it
	integerFile.close()
	
	return integerList


# Ask the user for their input
def AskUserFrequency():

	# input for finding frequent values in the list
	while True:
		frequencyLevel = input("Enter an integer for frequency ranking, N (1 for most frequent, 2 for second most frequent, etc.): ")
		print()
		if represents_int(frequencyLevel):
			return int(frequencyLevel)
		else:
			print("Invalid. Please enter an integer.")
	

def ProcessTallyCount (tallyCount):
	# Expect a 2D list of data values and their frequencies
	# e.g. : [ [2,5] , [3,4] , [5, 4]]
	# Generate a new 2D list of frequencies with their corresponding data value(s)
	# e.g [ [5, 2] , [4, 3, 5] ]

	#First sort the tallyCount by Frequency (the second column) so that we can binarySearch it
	quickSort2D(tallyCount, 1)
	frequencyTable = []
	for rowIndex in range(0, len(tallyCount)):
		
		thisFrequency = tallyCount[rowIndex][1]
		thisDataValue = tallyCount[rowIndex][0]

		#Search the frequency table to see if we already have a row for this frequency
		foundIndex = binarySearch(frequencyTable, thisFrequency)

		if foundIndex > -1:
			# If found, pull the frequency row, and append the data value to the end			
			foundRow :list[int] = frequencyTable[foundIndex]
			foundRow.append(thisDataValue)
		else:
			frequencyTable.append([thisFrequency, thisDataValue])
			
	return frequencyTable

def RankFrequencies(frequencyTable):
	# Make a league table of descending frequencies and ascending data values
	# e.g. 
	#
	# Given an unordered input frequencyTable as follows:
	#
	#	|Frequency | Data Values
	#	| 1		   | 1, 2, 55 ,56, 99, 654
	#	| 4		   | 3
	# 	| 3		   | 4, 3, 2
	#
	# ... we want to generate the following:
	#
	#	| Rank | Frequency | *Lowest* Data Value
	#	| ASC  | DESC      | 
	#	|    1 |   4       | 3
	#	|    2 |   3       | 2
	#	|    3 |   1       | 1


	# When user asks for N=3, i.e. 3rd most frequent, we look up Rank = 3 in this table.

	#First make sure frequencyTable is sorted by frequency (column 0)
	quickSort2D(frequencyTable, 0)

	#Make a new league table
	leagueTable : list[list[int]] = []

	# Walk the frequencyTable *backwards*, reading the highest frequencies first
	currentRank = 1
	for rowIndex in range(len(frequencyTable)-1, -1, -1):

		# Note the current frequency row
		currentRow = frequencyTable[rowIndex]

		# Note the current frequency
		currentFrequency = currentRow[0]
		
		if len(currentRow) == 2:
			# This means there is only one data value with this frequency
			# So let's note the current data value:
			currentDataValue = currentRow[1]

			# So we just record it in the league table:
			leagueTable.append([currentRank, currentFrequency, currentDataValue])

			# Increment the rank, ready for the next row
			currentRank += 1
		else:
			# This means there are multiple data values at the SAME frequency,
			# and we need to add the *lowest* data value *only* to the league table.

			# So first get the data columns without the frequency (so skip index 0)
			currentRowDataValues = currentRow[1:len(currentRow)]

			# Sort the data values ascending
			quickSort(currentRowDataValues)

			# Copy first (lowest) data value to the league table
			leagueTable.append([currentRank, currentFrequency, currentRowDataValues[0]])

			#Increment currentRank for the next row
			currentRank += 1			

	return leagueTable

# Format a 2D list for the screen
def print2DList(TwoDlist):
	#Print out a row per line
	for row in range(0, len(TwoDlist)):
		print(TwoDlist[row])

#Validate user input - not longer than array
def ValidateUserInputNotTooBig(userFrequencyIndex, rankedFrequencyTable):
	if userFrequencyIndex > len(rankedFrequencyTable) -1:
		numFrequencies = len(rankedFrequencyTable)
		print("You requested N =", userFrequencyIndex + 1, "but we only found", numFrequencies, "frequenc", end="")
		if numFrequencies == 1:
			print("y. Showing the least frequent below:")
		else:
			print("ies. Showing the least frequent below:")
		print()

		userFrequencyIndex = len(rankedFrequencyTable) -1

	return userFrequencyIndex

#Validate user input - not shorter than array
def ValidateUserInputNotTooSmall(userFrequencyIndex):	
	if userFrequencyIndex < 0:
		print("You requested N =", userFrequencyIndex + 1, "so we are showing the *most* frequent below.")	
		print()	
		userFrequencyIndex = 0

	return userFrequencyIndex

# Format and output the results
def ReportFindings(userFrequencyIndex, rankedFrequencyTable):

	userFrequencyIndex = ValidateUserInputNotTooBig(userFrequencyIndex, rankedFrequencyTable)
	userFrequencyIndex = ValidateUserInputNotTooSmall(userFrequencyIndex)

	userRequestedDataValue = rankedFrequencyTable[userFrequencyIndex][2]
	print("User Frequency (N):", userFrequencyIndex + 1)
	print("User data:", userRequestedDataValue)
	print("Frequency of user data:", rankedFrequencyTable[userFrequencyIndex][1])

# Reads the integer file and allows user to pick Nth most frequent
def main():	

	# Read the input file
	integerList = ReadIntsFromFile(inputPath)

	# Validate the input
	if len(integerList) < 1:
		print("The input file has no valid data. Exiting.")
		print()
		return

	# Show the integer list
	print("Source Integer List:")
	if len(integerList) < 50:
		#Print the whole thing if small
		print(integerList)
	else:
		#Print the first few if massive
		for i in range(0, 20):
			print(integerList[i], ",", end="")
		print("...")
	print()
	
	# Ask the user
	userFrequencyIndex = AskUserFrequency() - 1

	# Count the inegers
	countedIntList = TallyUpIntegers(integerList)
	print("Tally Count:")
	print("| Integer | Count of Integer |")
	print2DList(countedIntList)
	print()

	# Gather up the frequencies, collapse duplicates
	frequencyTable = ProcessTallyCount(countedIntList)
	print("Frequency Table:")
	print("| Frequency | Integers... |")
	print2DList(frequencyTable)
	print()

	# Rank the frequencies
	rankedFrequencyTable = RankFrequencies(frequencyTable)
	print("Ranked Frequency Table:")
	print("| Ranking | Frequency | Integer |")
	print2DList(rankedFrequencyTable)
	print()

	# Output findings
	ReportFindings(userFrequencyIndex, rankedFrequencyTable)

main()