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
        if self.N > self.D:
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

class Question:

    def __init__(self, questionNumber: int):
        
        self.QuestionNumber = questionNumber        
        
        # Keep trying until the question has only non-whole improper fractions
        # And until the answer is also not whole
        while True:
            #Generate a pair of improper fractions that are not accidentally whole numbers
            self.f1 = self.GetNonWholeImproperFraction()
            self.f2 = self.GetNonWholeImproperFraction()


            #TODO random arithmetic operation
            

            self.CorrectAnswer = self.PerformRandomOperation()

            # Make sure Correct answer is also not whole
            if self.CorrectAnswer.IsWhole() == False:
                return

    def PerformRandomOperation(self):
        # Select an arithmetic operation at random and perform it on 
        # the two fractions, storing the operator symbol for display
        
        opIndex = random.randint(1, 4)
        
        if opIndex == 1:
            self.OperatorSymbol = "+"
            return self.f1.Add(self.f2)
        
        if opIndex == 2:
            self.OperatorSymbol = "-"
            return self.f1.Subtract(self.f2)
        
        if opIndex == 3:
            self.OperatorSymbol = "X"
            return self.f1.Multiply(self.f2)
        
        self.OperatorSymbol = " / "
        return self.f1.Divide(self.f2)
        
    def GetNonWholeImproperFraction(self):

        # Make a fraction with random numbers -15 to +15
        f1 = Fraction(self.RandomNumerator15(), self.RandomDenominator15())

        # Make sure its actually improper, and not accidentally a whole number
        while True:
            if f1.IsWhole() == False and f1.IsImproper() == True:
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
        return f"Question {self.QuestionNumber}: What is {self.f1} {self.OperatorSymbol} {self.f2} ?"
    
    def CheckAnswer(self, answer: "Answer"):
        if self.CorrectAnswer.Equals(answer.AnswerFraction):
            return "Correct!"
        return f"WRONG! The correct answer in lowest terms is {self.CorrectAnswer}."

class Answer:
    
    def ReadAnswer(self):
        self.AnswerString = input("Enter your answer as 'n/d' : ")
        if self.AnswerString == "":
            #Quitting
            return
        
        ns, ds = self.AnswerString.split("/")
        n = int(ns)
        d = int(ds)
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
