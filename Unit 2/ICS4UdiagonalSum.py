import random

numRows = int(input("Enter a number:"))
print("")
numColums = int(input("Enter a number:"))

square2DList = []

for i in range(0, numRows):
    row = []
    for j in range(0, numColums):
        randomNumber = random.randint(1,9)
        row.append(randomNumber)

    square2DList.append(row)
    print(square2DList[i])

print("")   


sumFirstDiagonal = 0
print("First diagonal", end = " ")
for x in range(0, numRows):
    sumFirstDiagonal += square2DList[x][x]
    print(square2DList[x][x], "+", end = " ")
print("=", sumFirstDiagonal)

print("")
sumSecondDiagonal = 0
print("Second diagonal", end=" ")
for y in range(numRows, 0, -1):
    sumSecondDiagonal += square2DList[y - 1][numRows - y]
    print(square2DList[y - 1][numRows - y], "+", end = " ")
print("=", sumSecondDiagonal)

sumOfDiagonals = sumFirstDiagonal + sumSecondDiagonal
print("")
print("The sum of the diagonals is ", sumOfDiagonals)
print("")
print(square2DList[2][0])

sumFirstVertical = 0
print("")

print("First Vertical", end = " ")
for x in range(0, numRows):
    sumFirstVertical += square2DList[x][0]
    print(square2DList[x][0], "+", end = " ")
print("=", sumFirstVertical)
