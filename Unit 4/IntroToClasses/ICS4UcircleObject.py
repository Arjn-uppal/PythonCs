class Circle:

    #Constructor for attributes
    def __init__(circle, radius):

        #Set the radius
        circle.radius = radius
        
    
    #Calculates the area
    def getArea(circle):
        
        #Calculation
        circle.radius = 3.14 * circle.radius**2

        return "Area of circle: " + str(circle.radius)
        

    #Calculates the circumference
    def getCircumference(circle, radius):
        
        #scale "circle.radius" value back down to radius value
        circle.radius = radius

        #Calculation
        circle.radius = 2 * 3.14 * circle.radius
        
        return "\nCircumference of circle: " + str(circle.radius) + "\n"


def main():
    
    #Creation of circle objects
    circleObject1 = Circle(5)
    circleObject2 = Circle(6)
    circleObject3 = Circle(10)
    circleObject4 = Circle(17)
    
    #Use area and circumference methods and display values
    print(circleObject1.getArea())
    print(circleObject1.getCircumference(5))
    print()

    print(circleObject2.getArea())
    print(circleObject2.getCircumference(6))
    print()

    print(circleObject3.getArea())
    print(circleObject3.getCircumference(10))
    print()

    print(circleObject4.getArea())
    print(circleObject4.getCircumference(17))



main()


