import timeit

#This recursive method
def doThisRecursive(x):    
    if x == 0:
        return 0
    else:
        return x % 10 + doThisRecursive(x // 10)

#This is a third way of braking up the integer inputed by the user into its singular digits and then making
#an array for those digits or characters of the integer. It then finds the sum of the character array
def doThisCharArray(x):
    digitsofX = [int(d) for d in str(x)]
    sumOfEntries = sum(digitsofX)
    return sumOfEntries

#The iterative method
def doThisIterative(x):
    temp_number = abs(x)
    sumOfDigits = 0
    while temp_number > 0:
        digit = temp_number % 10
        sumOfDigits += digit
        temp_number //= 10
    return sumOfDigits

#This method figures out the time elapsed for each method that adds the digits of the inputed integer.
#It allows the program to not have repeated "timeit" objects and print statements
def TimeFunction(x, functionType):
    start = timeit.default_timer()    
    if functionType == "Recursive":        
        sumOfDigits = doThisRecursive(x)

    elif functionType == "Iterative":
        sumOfDigits = doThisIterative(x)

    else:
        sumOfDigits = doThisCharArray(x)

    end = timeit.default_timer()

    #This increases the scope of the variable, "elapsedNS", so that it can be used in the main method 
    #for calculating a scalar value when you compare the time elapsed for both recursive and iterative methods  
    global elapsedNS
    elapsedNS = round((end - start)*10**9)
      
    print(functionType, "Solution took", elapsedNS, "nanoseconds\n")
    return sumOfDigits

def getInt(prompt):
    #Ask for an integer and validate before returning
    while True:
        inputString = input(prompt)
        if inputString.isdigit():
            return int(inputString)
        
def main():
    #Input
    print("")
    x = getInt("Enter an integer:")
    print("")

    #Recursive
    TimeFunction(x, "Recursive")
    recursiveTime = elapsedNS

    #Iterative
    TimeFunction(x, "Iterative")
    iterativeTime = elapsedNS

    #Iterative with a Char Array
    sumOfDigits = TimeFunction(x, "Char Array")

    print("The sum of the digits in the number", x, "is", sumOfDigits)
    print("The iterative algorithm is", round(recursiveTime / iterativeTime, 1), "times faster than the recursive one.")

#Time starts at zero and can be applied to multiple methods    
elapsedNS = 0
main()