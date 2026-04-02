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

        displayA = self.DontShow1ForA(self.A)
        displayB = self.DontShow1ForB(self.B)
        displayC = self.DontShow1ForC(self.C)

        # Using the unicode escape sequence for superscript-2 (\u00b2)
        return "y = " + displayA + "x\u00b2 " + displayB + "x " + displayC
    
    def DontShow1ForA(self, coefficientCouldBe1):
        # When A is 1 or -1 we don't need to diplay the "1" or the "-" sign

        display = str(coefficientCouldBe1)
        if coefficientCouldBe1 == 1:
            display = ""

        if coefficientCouldBe1 == -1:
            display = "-"
        
        return display
    
    def DontShow1ForB(self, coefficientCouldBe1):
        # When B is 1 or -1 we don't need to diplay the "1"
        # we just need the "+" or "-" sign    
        
        if coefficientCouldBe1 == 1:
            return "+ "

        if coefficientCouldBe1 == -1:
            return "-"

        display = str(coefficientCouldBe1)

        if coefficientCouldBe1 > 0 :
            return "+ " + display
        
        #B is negative but not -1
        return display
    
    def DontShow1ForC(self, coefficientCouldBe1):
        # When C is 0, don't show it
        # When C is positive we prefix a "+" sign.
        # When C is negative, str includes the "-" sign.
        
        if coefficientCouldBe1 == 0:
            return ""

        display = str(coefficientCouldBe1)

        if coefficientCouldBe1 < 0:
            return display
        
        # C is positive so prefix a "+" sign
        return "+ " + display
        
        
def main():

    quad1 = Quadratic(5, -2, 0.5)

    print(quad1.StandardForm())

main()