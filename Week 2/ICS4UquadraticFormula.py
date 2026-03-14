import numpy as np

#Inputs
aVal = int(input("What is your a value?"))
bVal = int(input("What is your b value?"))
cVal = int(input("What is your c value?"))

#Displaying Standard Form
print("")
print("Your standard form equation is as follows: ", aVal, "x^2", " + ", bVal, "x", " + ", cVal, sep='')

discriminant = bVal * bVal - (4 * aVal * cVal)

if discriminant < 0:
    print("There are no real roots")
    
else:
    #The Quadratic formula
    rootDiscriminant = np.sqrt(discriminant) 

    x1 = (-(bVal) + rootDiscriminant) / 2 * aVal
    x2 = (-(bVal) - rootDiscriminant) / 2 * aVal

    if x1 == x2:
        print("There is one real root:", x1)
    else:
        print("There are two real roots:", x1, "and", x2)
