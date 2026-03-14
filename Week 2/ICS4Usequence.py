#Input
userInput = int(input("Type a positive integer:"))

#Print first # of sequence
print(userInput, end = " ")

#Loop until x = 1
while True:

    #Is userInput even?
    if userInput % 2 == 0:
        #Divide by 2 
        userInput = userInput // 2
    else:
        #Multiply by 3 and add 1
        userInput = userInput * 3 + 1

    #Print new value 
    print(userInput, end = " ")

    #Stop when userInput = 1
    if userInput == 1:
        break