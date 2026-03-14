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


def main():
    a = [39,65,2,1,67,54,98,34,9,6]
    a = selectionSort(a)
    print(a)


main()