#Multiplies two positive integers
def multiply(a,b):
    if a == 0:
        return 0
    else:
        #This is where method calls itself and subtracts 1 from a
        #which is essential for preventing the method from calling itself infinitly
        return b + multiply(a-1, b)

def count3(N):

    if N == 0:
        return 0
    else:
        return 3 + count3(N-1)

def getInt(prompt):
    #Ask for an integer and validate before returning
    while True:
        inputString = input(prompt)
        if inputString.isdigit():
            return int(inputString)
        
#Main method that calls multiply method
def main():

    print("")

    #Inputs
    a = getInt("Enter a positive integer:")

    b = getInt("Enter another positive integer:")

    print("")
    print(multiply(a, b))
    print("")


main()