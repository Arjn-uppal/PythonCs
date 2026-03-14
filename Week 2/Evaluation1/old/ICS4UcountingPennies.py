import math

def Check_Point_Pos(radius):
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

def main():
    userRadius = int(input("What positive integer radius do you want:"))
    xyFit = Check_Point_Pos(userRadius)
    print("There are", xyFit, "pennies in a circle of radius", userRadius)

main()