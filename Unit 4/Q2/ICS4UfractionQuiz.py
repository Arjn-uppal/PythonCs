#imports ------------------------------------------

import math
import random

#Classes for Objects ------------------------------

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

    def IsWhole(self):
        if self.N % self.D == 0:
            return True
        return False
    
    def IsImproper(self):
        #First make a copy of the numerator
        nCopy = self.N

        #Check if the numerator is negative
        if nCopy < 0:
            nCopy = -1 * nCopy

        # Now if the absolute value of the numerator is more than the denominator
        # the fraction is improper
        if nCopy > self.D:
            return True
        return False

    def Reduce(self):

        # Finds the greatest common divisor
        # Of both the numerator and denominator
        gcd = math.gcd(self.N, self.D)

        # Modifies the calling object
        self.N = self.N // gcd
        self.D = self.D // gcd

    def Equals(self, other: "Fraction"):
        # Checks for OBJECT equality.
        # So DOES NOT reduce fractions first
        # Make sure both numerators and denominators match

        if self.N == other.N and self.D == other.D:
            return True
        
        return False
    
    def MathEquals(self, other: "Fraction"):
        # Checks for MATHEMATICAL equality.
        # So reduce both fractions first
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

class Question:

    def __init__(self, questionNumber: int):
        
        self.QuestionNumber = questionNumber        
        
        # Keep trying until the question has only non-whole improper fractions
        # And until the answer is also not whole
        while True:
            #Generate a pair of improper fractions that are not accidentally whole numbers
            self.f1 = self.GetNonWholeImproperFraction()
            self.f2 = self.GetNonWholeImproperFraction()

            self.CorrectAnswer = self.PerformRandomOperation()

            # Make sure Correct answer is also not whole
            if self.CorrectAnswer.IsWhole() == False:
                return

    def PerformRandomOperation(self):
        # Select an arithmetic operation at random and perform it on 
        # the two fractions, storing the operator symbol for display

        opIndex = random.randint(1, 4)
        
        if opIndex == 1:
            self.OperatorSymbol = " + "
            return self.f1.Add(self.f2)
        
        if opIndex == 2:
            self.OperatorSymbol = " - "
            return self.f1.Subtract(self.f2)
        
        if opIndex == 3:
            self.OperatorSymbol = " X "
            return self.f1.Multiply(self.f2)
        
        self.OperatorSymbol = " / "
        return self.f1.Divide(self.f2)
        
    def GetNonWholeImproperFraction(self):

        # Make a fraction with random numbers -15 to +15
        f1 = Fraction(self.RandomNumerator15(), self.RandomDenominator15())

        # Make sure its actually improper, and not accidentally a whole number
        while True:
            if f1.IsWhole() == False and f1.IsImproper() == True:
                f1.Reduce()
                return f1
            
            #Try again
            f1 = Fraction(self.RandomNumerator15(), self.RandomDenominator15())

    def RandomNumerator15(self):

        while True:
            randInt =  random.randint(-15, 15)
            if randInt != 0:
                return randInt
            
    def RandomDenominator15(self):
            return random.randint(1, 15)
    
    def __str__(self):

        #Add brackets around the second fraction if it is negative
        secondFractionDisplay = str(self.f2)
        if self.f2.N < 0:
            secondFractionDisplay = f"( {self.f2} )"

        return f"Question {self.QuestionNumber} :  What is  {self.f1} {self.OperatorSymbol} {secondFractionDisplay} ?"
    
    def CheckAnswer(self, answer: "Answer"):
        if self.CorrectAnswer.Equals(answer.AnswerFraction):
            return "\n************\n* Correct! *\n************\n"
        return f"WRONG! The correct answer in lowest terms is {self.CorrectAnswer}."

class Answer:
    
    # Make sure the string holds an integer
    def represents_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    
    def ReadAnswer(self):
        validAnswer = False
        while validAnswer == False:
            self.AnswerString = input("Enter your answer as 'n/d' : ")
            if self.AnswerString == "":
                #Quitting
                return
            
            # Must contain '/'
            slashPosition = self.AnswerString.find('/')
            if slashPosition == -1:
                print("You must enter a fraction including the '/' symbol")                
                continue

            #Slash must not be at the beginning or end
            if slashPosition == 0 or slashPosition == len(self.AnswerString)-1:
                print("The '/' symbol must be between two integers")
                continue
            
            #Must contain only one '/'
            elements = self.AnswerString.split("/")
            if len(elements) != 2:
                print("Enter a fraction with only one '/' symbol.")
                continue

            #Both elements must be integers
            if self.represents_int(elements[0]) == False or self.represents_int(elements[1]) == False:
                print("Please enter integers only for the numerator and denominator.")
                continue

            validAnswer = True
        
        n = int(elements[0])
        d = int(elements[1])
        self.AnswerFraction = Fraction(n, d)


class Quiz:

    def WelcomeMessage(self):
        print()
        print("Welcome to the Fractions Quiz!")
        print("------------------------------")
        print()
        print("Enter each answer in the form 'n/d'. Remember to give answer in lowest form.")
        print("Enter blank '' to quit.")
        print("Good luck!")
        print()

    def NextQuestion(self, questionNumber: int):
        q1 = Question(questionNumber)
        print(q1)
        print()
        return q1

    def NextAnswer(self):
        a1 = Answer()
        a1.ReadAnswer()
        return a1

    def CheckAnswer(self, question: "Question", answer: "Answer"):
        print(question.CheckAnswer(answer))
        print()

    def Exit(self, questionNumber):
        print()
        print("----------------------------------------------------------------")
        print(f"Thank you for attempting {questionNumber} questions. Goodbye!")
        print("----------------------------------------------------------------")
        print()

    def Start(self):
        self.WelcomeMessage()

        questionNumber = 1
        #Ask new questions until they quit
        while True:
            q1 = self.NextQuestion(questionNumber)
            a1 = self.NextAnswer()
            
            #Check for quitting
            if a1.AnswerString == "":
                break

            self.CheckAnswer(q1, a1)
            questionNumber += 1
            
        self.Exit(questionNumber)
        

#Functions for Main Program -----------------------

#Main Program -------------------------------------

def main():
    
    quiz = Quiz()
    quiz.Start()
       

main()
