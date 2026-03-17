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

#Create a list of integers of any given length
def CreateNumList(listLength):
    numList = []
    for i in range(listLength):
        numList.append(random.randint(1, 3000))
    return numList

#Create 100 lists of integers each left in a random unsorted order
#for the average case
def Create100Lists(listLength):
    listOf100Lists = []
    for i in range(100):
        listOf100Lists.append(CreateNumList(listLength))

    return listOf100Lists


#Create 100 lists of integers each pre-sorted in ascending order
#for the best case
def Create100SortedLists(listLength):
    listOf100Lists = []
    for i in range(100):
        listOf100Lists.append(insertionSort(CreateNumList(listLength)))

    return listOf100Lists

#Create 100 lists of integers each reverse-sorted in descending order
#for the worst case
def Create100ReverseSortedLists(listLength):
    listOf100Lists = []
    for i in range(100):
        sortedList = insertionSort(CreateNumList(listLength))

        #reverse the sorted list
        reverseList = []
        for n in range(len(sortedList)-1, -1, -1):
            reverseList.append(sortedList[n])

        listOf100Lists.append(reverseList)

    return listOf100Lists

#Measure the average time to sort 100 lists
def AverageTime100Sorts(lists):

    #Running total of all 100 execution times
    runningTotalTime = 0
    for list in lists:
        #Time the sorting of each list
        start = timeit.default_timer()
        insertionSort(list)
        end = timeit.default_timer()
        time = end - start
        
        #Increment running total
        runningTotalTime += time

    #During testing noticed with a manual stop watch that 0.086 from timeit actually is 8.6 seconds
    #So I am treating timeit values as hectoseconds (s * 10^2)

    #Calculate the average
    averageExecutionHectoSeconds = runningTotalTime / len(lists)

    #Convert hectoseconds to milliseconds
    averageExecutionMilliSeconds = averageExecutionHectoSeconds * 100000

    #Trial runs show that even with the smallest list of 200 items, whole milliseconds are accurate enough
    #So truncate to int
    return int(averageExecutionMilliSeconds)

def AverageCaseExperiment():
    #Do 100 experiments using the Average case (100 random unsorted lists)
    print("Average Case Timings")
    print("| List Length | Execution Time |")
    for listLength in range(200, 3200, 200):
        lists = Create100Lists(listLength)
        print(listLength, AverageTime100Sorts(lists), sep=",")

def BestCaseExperiment():
    #Do 100 experiments using the Best case (100 pre-sorted lists)
    print("Best Case Timings")
    print("| List Length | Execution Time |")
    for listLength in range(200, 3200, 200):
        lists = Create100SortedLists(listLength)
        print(listLength, AverageTime100Sorts(lists), sep=",")

def WorstCaseExperiment():
    print("Worst Case Timings")
    print("| List Length | Execution Time |")
    #Do 100 experiments using the Worst case (100 reverse-sorted lists)
    for listLength in range(200, 3200, 200):
        lists = Create100ReverseSortedLists(listLength)
        print(listLength, AverageTime100Sorts(lists), sep=",")

def main():

    #Do 100 experiments using the Average case (100 random unsorted lists)
    AverageCaseExperiment()

    #Do 100 experiments using the Best case (100 pre-sorted lists)
    BestCaseExperiment()

    #Do 100 experiments using the Worst case (100 reverse-sorted lists)
    WorstCaseExperiment()

main()