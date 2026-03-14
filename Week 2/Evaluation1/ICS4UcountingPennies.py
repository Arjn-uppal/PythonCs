import math
def isPointInCircle(x, y, radius):
    # This function tests if any point (x,y) is in or on the circle
    # By Pythagoras a point is inside a circle if 
    # (x**2) + (y**2) <= radius**2
    return (x**2) + (y**2) <= radius**2

def CountPenniesInsideCircle(radius):
    # This is an alternate function I wrote that uses the symmetry of 
    # circles centered at the origin to count the pennies that will fit.

    # Equation of a circle where center is at origin
    # radius**2 = (x**2) + (y**2)   
    # => y = math.sqrt((radius**2) - ((x)**2))

    pointCount = 0
    x = 0
    while x <= radius:
        #Starting at 0, let's step out along the x-axis towards the circle

        #Calculate y at this x position
        y = math.sqrt((radius**2) - ((x)**2))

        #Formula used for figuring out the number of integer points (pennies) for the current x value
        # Truncate the y down to its integer part
        # Double that to count the pennies both above and below the x axis
        # Finally add 1 for the penny on the x axis itself (y=0)

        verticalPointsAtX = 2*(int(y)) + 1
        if x == 0:
            # if we're at the origin, just count this column of pennies once
            pointCount += verticalPointsAtX
        else:
            # otherwise, count this columns of pennies twice, once for x and once for -x
            pointCount += 2 * verticalPointsAtX

        #Move over to the next x position
        x += 1
        
    return pointCount

def CountWithTestFunction(radius):
    #In this function I try to choose efficiently which points need testing
    # and to count the pennies using what we know about the symmetry of the circle.

    if radius <= 0:
        return 0
    
    pointCount = 2 # We count the two pennies at x = +/- radius already
    x = 0
    y = radius - 1
    while x <= radius -1:
        # Along the y-axis we have an easy formula for penny points
        if x == 0:
            # no need to test points.
            pointCount += 2 * radius + 1
        else:
            # We know that (x,r) is now outside the circle
            # So lets test (x, r-1) (we only care about integers)            
            while y >= 0:
                if isPointInCircle(x, y, radius):
                    #Count each penny twice (above and below x-axis) and add one for the x-axis itself
                    # = 2y+1
                    #Then double that for the left side of the y-axis
                    # = 2(2y+1)
                    # = 4y+2
                    pointCount += 4 * y + 2
                    break
                else:
                    y = y - 1


        x += 1

    return pointCount

def getInt(prompt):
    #Ask for an integer and validate before returning
    while True:
        inputString = input(prompt)
        if inputString.isdigit():
            return int(inputString)

def main():
    userRadius = getInt("Enter a positive integer for the radius:")
    #xyFit = CountPenniesInsideCircle(userRadius)
    xyFit = CountWithTestFunction(userRadius)
    print("There are", xyFit, "pennies in a circle of radius", userRadius)

main()