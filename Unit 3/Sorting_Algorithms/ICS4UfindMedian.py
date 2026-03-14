#a is the list to sort
#This algorithm sorts in ascending order (smallest to biggest)

def selectionSort(a):
    small = 0
    smallIndex = 0

    for i in range(0, len(a)):

        #Sets the minimum to the first non sorted location
        small = a[i]

        #Search the rest of the list for the smallest value
        for j in range(i, len(a)):

           #Found a new smallest? record its location too.
           if a[j] <= small:
               small = a[j]
               smallIndex = j

        #Make the swap
        a[smallIndex] = a[i]
        a[i] = small

    return a

#(len - 1) / 2
def findMedian(sortedA):

    #Odd
    if len(sortedA) % 2 == 1:
        middleIndex = round((len(sortedA) - 1) / 2, None)
        middleVal = sortedA[middleIndex]
        return middleVal
    
    #Even
    else:
        fstMiddleIndex = round((len(sortedA) - 2) / 2, None)
        secMiddleIndex = round(len(sortedA) / 2, None)

        fstMiddleVal = sortedA[fstMiddleIndex]
        secMiddleVal = sortedA[secMiddleIndex]

        middleValAverage = (fstMiddleVal + secMiddleVal) / 2
        return middleValAverage


def main():
    a = [39,65,2,1,67,101,102,98,34,9,6]
    sortedA = selectionSort(a)

    print(sortedA)
    print()
    print("The median:")

    median = findMedian(sortedA)
    print(median)


main()