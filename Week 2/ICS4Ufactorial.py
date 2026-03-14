def factorial(userInput):

    if userInput == 1:
        return 1
    else:
        return userInput * factorial(userInput - 1)


def main():

    userInput = int(input("Enter a positive integer:"))
    x = factorial(userInput)
    print(x)


main()