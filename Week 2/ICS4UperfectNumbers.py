def perfectNumberEuler():
    #I started out trying this Euclid-Euler function but did not have time to make it work.
    #I went back to finding the factors by hand
    for i in range(1, 500):
        
        #Euclid-Euler Theorem
        x = 2**(i-1)
        y = (2**i) - 1
        n = x*y

#Find Factors of x / candidate
def FindFactors(x, w):
    for i in range(w, x + 1):
        fCan1 = x / i
        fCan = x % i 

        #This returns the factor that produces a whole number
        if fCan == 0:
            return fCan1

#Sum up all the entries of the simplified factor list, oneFactorEach, and check if
#the candidate is a perfect number
def addFactors(candidate, oneFactorEach):
    sumFactors = sum(oneFactorEach)

    if sumFactors == candidate:
        print(candidate, " ", end="")

#This is where all the methods are called
def main():
    print("The perfect numbers between 1 and 500 are: ", end="")

    #This is the range of numbers from 1 to 500
    for candidate in range(1, 501):

        #This list is used to store all possible factors of candidate 
        factorList = []

        #This represents the divisor of candidate in order to find factors.
        #It starts at two instead of 1 so that it excludes the candidate itself as a factor
        w = 2

        #This for loop calls a function that finds factors multiple times
        #and therefore, returns factors multiple times. This return statement breaks
        #out of the function which is why the for loop is used to call the function again
        for y in range(1, candidate):
            factorPerfect = FindFactors(candidate, w)

            #factors that produce whole numbers are added to the empty list, factorList.
            factorList.append(factorPerfect)

            #This allows multiple numbers to be checked for perfect factors from 2 to candidate
            w = w + 1
        
        #These two lines remove the duplicate factors and make a list of simplified, one of a kind, factors
        uniqueFactors = set(factorList)
        oneFactorEach = list(uniqueFactors)

        addFactors(candidate, oneFactorEach)

print("")
main()