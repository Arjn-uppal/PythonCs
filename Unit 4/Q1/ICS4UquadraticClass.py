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
    
def main():

    quad1 = Quadratic(5, -1, -2)

    print(quad1.StandardForm())
    print()
    print ("h = " + str(quad1.h))
    print(quad1.VertexForm())

main()