import math

class Quadratic:

    #Standard Form  : y = Ax^2 + Bx + C

    #Vertex Form    : y = A(x-h)^2 + k

    # Constructor
    def __init__(self, quadraticCoeft, linearCoeft, constantTerm):

        #Set the quadratic coefficient "A"
        self.A = quadraticCoeft

        #Set the linear coefficient "B"
        self.B = linearCoeft

        #Set the constant term "C"
        self.C = constantTerm

        #Calculate coefficients for vertex form
        # h = -B / 2A
        self.h = -1 * (self.B / (2 * self.A))

        #Substitute x=h in the standard form
        # k = Ah^2 + Bh + C
        self.k = (self.A * self.h * self.h) + (self.B * self.h) + self.C

    def StandardForm(self):

        #To display Standard Form  : y = Ax^2 + Bx + C        
        
        return self.DisplayA() + self.DisplayB() + self.DisplayConstant(self.C)
    
    def DisplayA(self):
        # When A is 1 or -1 we don't need to diplay the "1" or the "-" sign
        
        display = str(self.A)        
        if self.A == 1:
            display = ""

        if self.A == -1:
            display = "-"
        
        # Prefix with "y = ".
        # Then append "x^2"using the unicode escape sequence for superscript-2 (\u00b2).
        return "y = " + display + "x\u00b2 "
    
    def DisplayB(self):
        # When B is 1 or -1 we don't need to diplay the "1"
        # we just need the "+" or "-" sign    
        
        if self.B == 1:
            return "+ x "

        if self.B == -1:
            return "-x "

        display = str(self.B)

        if self.B > 0 :
            return "+ " + display + "x "
        
        #B is negative but not -1
        return display + "x "
    
    def DisplayConstant(self, constantTerm):
        #For displaying constants like C or k

        # When constantTerm is 0, don't show it
        # When constantTerm is positive we prefix a "+" sign.
        # When constantTerm is negative, str includes the "-" sign.
        
        if constantTerm == 0:
            return ""

        display = str(constantTerm)

        if constantTerm < 0:
            return display
        
        # constantTerm is positive so prefix a "+" sign
        return "+ " + display
        
    def VertexForm(self):
        
        # To display Vertex Form    : y = A(x-h)^2 + k

        return self.DisplayAVertex() + self.DisplayH() + self.DisplayConstant(self.k)
        
    def DisplayAVertex(self):
        # When A is 1 or -1 we don't need to diplay the "1" or the "-" sign
        
        display = str(self.A)        
        if self.A == 1:
            display = ""

        if self.A == -1:
            display = "-"
        
        # Prefix with "y = ".        
        return "y = " + display

    def DisplayH(self):
        #In Vertex form, h is subtracted from x, so we need to flip signs 

        #First negate h
        negativeH = -1 * self.h

        # If that's positive, add a "+" sign
        if negativeH > 0:
            return "(x + " + str(negativeH) + ")\u00b2 "
        
        # otherwise add a "-" sign
        return "(x - " + str(self.h) + ")\u00b2 "
    
    def OpeningDirection(self):
        if self.A > 0:
            return "Up"
        
        return "Down"
    
    def VertexCoordinates(self):
        coordinates = [self.h, self.k]
        return coordinates
    
    def YIntercept(self):
        # This happens when x = 0
        # So we substitute x = 0 in the equation
        # Y = (A)(0)^2 + B(0) + C
        # Y = C
        return self.C
    
    def XIntercepts(self):
        # Using the Quadratic formula to find the X - Intercepts        

        # X-intercept list        
        roots = []
        
        # The discriminant in the quadratic formula
        dSquared = (self.B * self.B) - (4 * self.A * self.C)

        # There are no real roots
        if dSquared < 0:
            return roots
        
        d = math.sqrt(dSquared)               
        
        roots.append(((-1 * self.B) + d) / (2 * self.A))

        # There is one real root
        if d == 0:            
            return roots
        
        # There are two real roots        
        
        roots.append(((-1 * self.B) - d) / (2 * self.A))                
        return roots
    
    def Add(self, addend: "Quadratic"):
        #Return a new Quadratic that is the sum of self and addend:
        return Quadratic(self.A + addend.A, self.B + addend.B, self.C + addend.C)

        
    
def main():
    # Demonstrate all the methods of the Quadratic class

    print()
    print("Demo of all methods of the Quadratic class")
    print("------------------------------------------")
    print()

    #Create our first quadratic using the constructor:
    quad1 = Quadratic(5, -2, -1)
    print("Create a quadratic with A=5, B=-2 and C=-1: Quadratic(5, -2, -1)")
    print("h for vertex form calculated as: " + str(quad1.h))
    print("k for vertex form calculated as: " + str(quad1.k))
    print()

    #Display in Standard Form:
    print("Display in Standard Form: quad1.StandardForm(): ")
    print(quad1.StandardForm())
    print()

    #Display in Vertex Form:
    print("Display in Vertex Form: quad1.VertexForm(): ")
    print(quad1.VertexForm())
    print()

    #Direction of opening
    print("Direction of opening: " + quad1.OpeningDirection())
    print()

    #Vertex Coordinates
    print("Vertex Coordinates: " + str(quad1.VertexCoordinates()))
    print()

    #Y-Intercept
    print("Y-Intercept: " + str(quad1.YIntercept()))
    print()

    #X-Intercepts
    print("X-Intercepts: " + str(quad1.XIntercepts()))
    print()

    #Create a second quadratic and add them together
    quad2 = Quadratic(-3, 3, 2)
    qSum = quad1.Add(quad2)
    print("Create a second instance of a quadratic with A=-3, B=3 and C=2.")
    print(quad2.StandardForm())
    print()

    print("Add the two instances together : qSum = quad1.Add(quad2)")
    print("The sum is : " + qSum.StandardForm())
    print("And in Vertex Form : " + qSum.VertexForm())
    print()

main()