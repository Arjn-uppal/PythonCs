file = open("dataOUT.txt", "w")

x = ["Connor", "Kyle", "Amber", "Jessica", "Winifred"]
y = [5, 15, 30, 17, 20]

for i in range(0, len(x)):
    line = x[i] + " " + str(y[i]) + "\n"
    file.write(line)

file.close()