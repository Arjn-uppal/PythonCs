
file = open("data.txt","r")

bankAccount = []

while True:
    line = file.readline().rstrip("\n")
    if line == "":
        break
    else:
        row = []
        
        tokens = line.split(" ")

        theName = tokens[0]

        theAmount = float(tokens[1])

        row.append(theName)
        row.append(theAmount)

        bankAccount.append(row)


file.close()

print(bankAccount)
print("")

for i in range(0, len(bankAccount)):
    for j in range(0, len(row)):
        print(bankAccount[i][j], end=" ")
    print("")
print("")




