inputPath = "MineGrid.txt"
outputPath = "MineFieldHints.txt"

#Tested with 14,500 lines in the input file

def main():
    #Read the input file
    #Scan the mine field counting neighbourhood mines
    #Write out findings

    print()
    mineArray = ReadMineFile()
    mineCountArray = ScanMineField(mineArray)
    WriteMineFile(mineCountArray)    
    print("Done.")

def ReadMineFile():

    #Open the file for reading
    minefile = open(inputPath, "r")

    #This is an empty list to store the data
    mineField = []

    #Reads each line in the text file and adds each line to a list and
    #adds the list to a 2D list

    print("Reading the input file...")
    mineFileLines = minefile.readlines()
    for mineFileLine in mineFileLines:
        mineRow = mineFileLine.rstrip("\n").split(" ")
        mineField.append(mineRow)        

    #File is completely read so close it
    minefile.close()
    print()
    return mineField

def CountNeighbourMines(mineArray, subjectX, subjectY):
    #The "subject" square is the one square that we are counting neighbouring mines for 
    #So subjectY is the index of the row of the subject square in the minefield
    #and subjectX is the index of the column of the subject square in the minefield

    neighbourMineCount = 0

    # For the rows one above the subject, to one below the subject
    for rowIndex in range(subjectY - 1, subjectY + 2):

        #Ignore the rows outside the minefield (when the subject is at one edge or a corner)
        if rowIndex >= 0 and rowIndex < len(mineArray):

            #For the columns from one to the left of the subject, to one to the right
            for colIndex in range(subjectX - 1, subjectX + 2):

                #Ignore columns outside the minefield (when the subject is at one edge or a corner)
                if colIndex >= 0 and colIndex < len(mineArray[subjectY]):

                    #if we find a mine here, count it
                    if mineArray[rowIndex][colIndex] == "*":
                        neighbourMineCount += 1                
    
    return neighbourMineCount

def ScanMineField(mineArray):
    #Walk the whole minefield row by row, column by column, and call the counting function

    print("Scanning the mine field...")
    #For each row of the minefield
    for rowIndex in range(0, len(mineArray)):

        #For each position (column) in the row
        for columnIndex in range(0, len(mineArray[rowIndex])):

            #If we are at a blank square (no mine)
            if mineArray[rowIndex][columnIndex] == ".":
                #Call the neighbourhood counting function for this square
                mineArray[rowIndex][columnIndex] = CountNeighbourMines(mineArray, columnIndex, rowIndex)

    print()            
    return mineArray

def WriteMineFile(mineCountArray):
    #This outputs the modified mine field by replacing the dots with numerical hints that depend
    #on the position of the mines (stars)

    print("Writing the output file...")

    #Open the file for writing too
    mineFieldFile = open(outputPath, "w")

    #Counts through every row of the minefield
    for rowIndex in range(0, len(mineCountArray)):

        #Counts through every column in each row
        for colIndex in range(0, len(mineCountArray[rowIndex])):

            #Writes each element of the minefield to the file
            mineFieldFile.write(str(mineCountArray[rowIndex][colIndex]))
            #print(str(mineCountArray[rowIndex][colIndex]), end=" ")

            #Write a space unless we're at the end of the row
            if colIndex < len(mineCountArray[rowIndex]) - 1:
                mineFieldFile.write(" ")
        
        #write a new line unless we're at the end of the rows
        if rowIndex < len(mineCountArray) - 1:
            mineFieldFile.write("\n")
            #print()

    #Close the file we are writing too
    mineFieldFile.close()
    print()

main()