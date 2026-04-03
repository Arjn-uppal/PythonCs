import math

class Fraction:

    #Constructor
    def __init__(self, numerator, denominator):

        # Set the numerator
        self.N = numerator

        # Set the denominator
        self.D = denominator

        # Calculate improper fraction
        self.improper = self.N / self.D

    def Reduce(self):

        # Finds the greatest common divisor
        # Of both the numerator and denominator
        gcd = math.gcd(self.N, self.D)

        # Modifies the calling object
        self.N //= gcd
        self.D //= gcd

    def Equals(self, otherFraction):

        # Compare the fractions by comparing their ratios with each other
        ratio2 = otherFraction.N / otherFraction.D

        # Returns true or false
        return self.improper == ratio2
    
    def __str__(self):
        # Returns a fraction in the form n / d
        return str(self.N) + "\n" + "-" + "\n" + str(self.D)
    
    def Add(self, otherFraction: "Fraction"):

        # First common denominator fraction
        fcdFraction = (self.N * otherFraction.D) / (self.D * otherFraction.D)

        # Second common denominator fraction
        scdFraction = (otherFraction.N * self.D) / (otherFraction.D * self.D)

        # Return a new fraction that is the sum of both fractions
        return Fraction(fcdFraction + scdFraction)
    
    def Subtract(self, otherFraction: "Fraction"):

        # First common denominator fraction
        fcdFraction = (self.N * otherFraction.D) / (self.D * otherFraction.D)

        # Second common denominator fraction
        scdFraction = (otherFraction.N * self.D) / (otherFraction.D * self.D)

        # Return a new fraction that is the difference of both fractions
        return Fraction(fcdFraction - scdFraction)
    
    def Multiply(self, otherFraction: "Fraction"):

        # Return a new fraction that is the multiple of both fractions
        return Fraction((self.N * otherFraction.N) / (self.D * otherFraction.D))
    
    def Divide(self, otherFraction: "Fraction"):

        # Return a new fraction that is the quotient of both fractions
        return Fraction((self.N * otherFraction.D) / (self.D * otherFraction.N))
    

def main():
    # Demonstrate all the methods of the Fraction class

    print()
    print("Demo of all methods of the Fraction class")
    print("------------------------------------------")
    print()

    # Create our first Fraction using the constructor:
    Fraction1 = Fraction(5, 4)
    print(str(Fraction1.D))

main()
