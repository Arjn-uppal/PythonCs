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
        return "Area of circle: " + circle.radius + "\nBalance: $" + str(self.balance) + "\n"


def main():



main()


