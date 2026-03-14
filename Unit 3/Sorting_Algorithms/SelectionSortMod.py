#a is the list to sort
#This algorithm sorts in ascending order (smallest to biggest)

def selectionSort(a):
    small = 0
    smallIndex = 0

    newA = a.copy()

    for i in range(0, len(newA)):

        #Sets the minimum to the first non sorted location
        small = newA[i]

        #Search the rest of the list for the smallest value
        for j in range(i, len(newA)):

           #Found a new smallest? record its location too.
           if newA[j] <= small:
               small = newA[j]
               smallIndex = j

        #Make the swap
        newA[smallIndex] = newA[i]
        newA[i] = small

    return newA


def main():
    a = [39,65,2,1,67,54,98,34,9,6]
    fixedList = selectionSort(a)
    print(fixedList)
    print(a)


main()