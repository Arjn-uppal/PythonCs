#a is the list to sort
#This algorithm sorts in ascending order (smallest to biggest)

def bubbleSort(a):

    #The number of "Bubble Cycles" is the length of the list
    for i in range(0, len(a)):

        #Cycle through all adjacent elements not yet sorted (reduces each time)
        for  j in range(1, len(a) - i):
            
            #Check for out of order and swap elements
            if a[j - 1] > a[j]:

                swapValue = a[j]
                a[j] = a[j - 1]
                a[j - 1] = swapValue

    return a

def main():
    a = [39,65,2,1,67,54,98,34,9,6]
    a = bubbleSort(a)
    print(a)

main()