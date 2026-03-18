class Circle:

    #Constructor for attributes
    def __init__(circle, radius):

        #Set the radius
        circle.radius = radius
        area = circle.radius
        circumference = circle.radius
        
    #Calculates the area
    def getArea(circle):
        
        #Calculation
        area = 3.14 * circle.radius**2
        
        
    #Calculates the circumference
    def getCircumference(circle):
        
        #Calculation
        circumference = 2 * 3.14 * circle.radius
        
        
    def __str__(circle):
        return "Area of circle: " + str(area) + "\nCircumference of circle: " + str(circumference) + "\n"


def main():
    
    #Creation of  circle objects
    circleObject1 = Circle(5)
    circleObject2 = Circle(6)
    circleObject3 = Circle(10)
    circleObject4 = Circle(17)
    
    #Use area and circumference methods
    circleObject1.getArea()
    circleObject1.getCircumference()
    
    #display results
    print(circleObject1)
    print()
    
    print(circleObject2)
    print()
    
    print(circleObject3)
    print()
    
    print(circleObject4)
    print()



main()


