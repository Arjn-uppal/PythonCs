import random
import timeit

#Quick Sort Functions:
def quickSort(a):
	sortPartition(a, 0, len(a) - 1)


def sortPartition(a, low, high):
	
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


def bubbleSort(a):

    #The number of "Bubble Cycles" is the length of the list
	for i in range(0,len(a)):

		#Cycle through all adjacent elements not yet sorted (reduces each time)
		for j in range(1,len(a)-i):

			#Check for out of order and swap elements
			if a[j-1] > a[j]:

				swapValue = a[j]
				a[j] = a[j-1]
				a[j-1] = swapValue
                        

#Function to generate random list
def genRandomList(n, min, max):
    
    a = []
    for i in range(0, n):
        a.append(random.randint(min, max))
    
    return a


#Copy an existing list into a new list
def copyList(a):
    
    newList = []
    for i in range(0, len(a)):
        newList.append(a[i])
    
    return newList


def main():
    
    #Generate a random list with 5000 elements between 0 and 20,000
    originalList = genRandomList(5000, 0, 20000)

    #Need copies of the list to give to all the sorting functions
    #because sort functions modifies original list
    bubbleList = copyList(originalList)
    QuickList = copyList(originalList)

    #Time bubble sort on the list
    start = timeit.default_timer()
    bubbleSort(bubbleList)
    end = timeit.default_timer()

    #Conversion
    bubbleTimeMicro = int((end - start) * 10**6)
    print("Bubble Time:", bubbleTimeMicro)

    #Time Quick sort on the list
    start = timeit.default_timer()
    quickSort(QuickList)
    end = timeit.default_timer()

    #Conversion
    quickTimeMicro = int((end - start) * 10**6)
    print("Quick Time:", quickTimeMicro)


main()