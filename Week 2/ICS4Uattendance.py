#Note: No input validation, only integers are accepted

#Input
totalClasses = int(input("How many classes are there in total: "))
studentAttendence = int(input("How many classes have you attended: "))

#Find and output % attended
proportionAttended = studentAttendence / totalClasses

print(f"You attended {proportionAttended:.0%} of your classes.")
print("")

#Determine if exam can be written
if proportionAttended < 0.75:
        print("You are not allowed to write the University exam")
else:
        print("You can write the University exam")