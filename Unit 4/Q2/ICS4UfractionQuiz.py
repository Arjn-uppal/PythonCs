import math

class Fraction:

    #Constructor
    def __init__(self, numerator: int, denominator: int):

        #denominator cannot be 0
        if denominator == 0:
            raise ValueError("Denominator must not be 0.")
        
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
        self.N = self.N // gcd
        self.D = self.D // gcd

    def Equals(self, other: "Fraction"):
        # Reduce both fractions.
        # Make sure both numerators and denominators match

        self.Reduce()
        other.Reduce()

        if self.N == other.N and self.D == other.D:
            return True
        
        return False        
    
    def __str__(self):
        # Returns a fraction in the form "n/d"
        return str(self.N) + "/" + str(self.D)
    
    def Add(self, other: "Fraction"):
        # Take any N1/D1 and N2/D2
        # Calculate the sum
        # Reduce the result and return

        # Ensure common denominators for both arguments

        # Common Denominator:
        if self.D == other.D:
            # Both arguments already have the same denominator
            fSum = Fraction(self.N + other.N, self.D)

        else:
            # Find and use a Common Denominator:
            commonDenominator = self.D * other.D

            # For self:
            # (N1 * D2) / commonDenominator

            # For other:
            # (N2 * D1) / commonDenominator

            f1 = Fraction(self.N * other.D, commonDenominator)
            f2 = Fraction(other.N * self.D, commonDenominator)

            fSum = Fraction(f1.N + f2.N, commonDenominator)

        fSum.Reduce()
        return fSum
    
    def Subtract(self, other: "Fraction"):

        # First negate the other
        negatedOther = Fraction(other.N * -1, other.D)

        # Add self to negatedOther
        return self.Add(negatedOther)
    
    def Multiply(self, other: "Fraction"):

        # Return a new fraction that is the multiple of both fractions
        fProduct = Fraction(self.N * other.N, self.D * other.D)
        fProduct.Reduce()
        return fProduct        
    
    def Divide(self, other: "Fraction"):

        # Return a new fraction that is the quotient of both fractions

        # Flip the other
        otherFlipped = Fraction(other.D, other.N)

        # Multiply self with otherFlipped
        fQuotient = self.Multiply(otherFlipped)
        fQuotient.Reduce()
        return fQuotient

def main():
    

    f1 = Fraction(3, 4)
    f2 = Fraction(0, 2)
        
    print(f1, f2)  
    print(f1.Add(f2))
    print(f1.Subtract(f2))
    print(f1.Multiply(f2))
    print(f1.Divide(f2))
       

main()
