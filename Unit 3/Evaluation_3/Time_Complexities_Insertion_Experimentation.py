import timeit

#a is the list to sort
#This algorithm sorts in ascending order (smallest to biggest)

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


def main():
    a = [39,65,2,1,67,54,98,34,9,6]

    start = timeit.default_timer()

    a = insertionSort(a)

    end = timeit.default_timer()

    time = end - start

    timeMilli = round(time * 10**3, 3)

    print(timeMilli)
    


main()