import timeit
import random

#Using the Insertion Sort code from class.
#a is the list to sort.
#This algorithm sorts in ascending order (smallest to biggest).
def insertionSort(a):

    #Cycle through all the elements in the list 1 -> end (Assume 0 index is sorted)
    for i in range(1, len(a)):

        #Take a value out of the list to insert in the already sorted list
        insertValue = a[i]

        #Find the correct spot in the already sorted list
        location = i
        while location > 0 and a[location - 1] > insertValue:

            a[location] = a[location - 1]
            location = location - 1

        #Now have found insertValue's location so insert it
        a[location] = insertValue

    return a

def CreateNumList(listLength):
    numList = []
    for i in range(listLength):
        numList.append(random.randint(1, 3000))
    return numList

def Create100SortedLists(listLength):
    listOf100Lists = []
    for i in range(100):
        listOf100Lists.append(insertionSort(CreateNumList(listLength)))

    return listOf100Lists

def Create100Lists(listLength):
    listOf100Lists = []
    for i in range(100):
        listOf100Lists.append(CreateNumList(listLength))

    return listOf100Lists

def Create100ReverseSortedLists(listLength):
    listOf100Lists = []
    for i in range(100):
        sortedList = insertionSort(CreateNumList(listLength))
        reverseList = []
        for n in range(len(sortedList)-1, -1, -1):
            reverseList.append(sortedList[n])

        listOf100Lists.append(reverseList)

    return listOf100Lists

def AverageTime100Sorts(lists):

    runningTotalTime = 0
    for list in lists:
        start = timeit.default_timer()
        insertionSort(list)
        end = timeit.default_timer()
        time = end - start
        runningTotalTime += time

    #During testing noticed with a manual stop watch that 0.086 from timeit actually is 8.6 seconds
    #So I am treating timeit values as hectoseconds (s * 10^2)

    #Calculate the average
    averageExecutionHectoSeconds = runningTotalTime / len(lists)

    #Convert hectoseconds to milliseconds
    averageExecutionMilliSeconds = averageExecutionHectoSeconds * 100000

    #Trial runs show that even with the smallest list of 200 items, whole milliseconds are accurate enough
    #So truncate to int
    return averageExecutionMilliSeconds

def AverageCaseExperiment():
    #Do 100 experiments using the Average case (100 random unsorted lists)
        for listLength in range(200, 3200, 200):
            lists = Create100Lists(listLength)
        print(listLength, AverageTime100Sorts(lists))

def BestCaseExperiment():
    #Do 100 experiments using the Best case (100 pre-sorted lists)
    for listLength in range(200, 3200, 200):
        lists = Create100SortedLists(listLength)
        print(listLength, AverageTime100Sorts(lists))

def main():

    #Do 100 experiments using the Average case (100 random unsorted lists)
    AverageCaseExperiment()

    #Do 100 experiments using the Best case (100 pre-sorted lists)
    #BestCaseExperiment()

    #lists = Create100ReverseSortedLists(20)
    #for list in lists:
        #print(list)

main()