inputPath = "Unit 3/Evaluation_3/InputFiles/002 letterDataValues.txt"

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

#Quick Sort adapted to sort a 2D list based on the zero element of each "row" array
#I use this to sort my frequency table
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

	integerFile = open(inputPath, "r")

	# Reads each line, converts string to int, and adds it to a list.
	# Stops reading the file when it gets to the end
	while True:
		singularInteger = integerFile.readline().rstrip("\n")

		if singularInteger == "":
			break
		else:
			if represents_int(singularInteger):
				trueInt = int(singularInteger)
				integerList.append(trueInt)

	# File is completely read so close it
	integerFile.close()
	
	return integerList
