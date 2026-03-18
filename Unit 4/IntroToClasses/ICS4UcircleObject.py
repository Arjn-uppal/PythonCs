class Circle:

    #Constructor for attributes
    def __init__(circle, radius):

        #Set the radius
        circle.radius = radius
        
    #Calculates the area
    def getArea(circle):
        
        #Calculation
        circle.radius = 3.14 * circle.radius**2
        
    #Calculates the circumference
    def getCircumference(circle):
        
        #Calculation
        circle.radius = 2 * 3.14 * circle.radius
        
    def __str__(circle):
        return "Area of circle: " + circle.radius + "\nBalance: $" + str(self.balance) + "\n"


def main():



main()


