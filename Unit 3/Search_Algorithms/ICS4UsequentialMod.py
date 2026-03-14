def everySighting(numericalList, target):
    locations = []

    for index in range(0, len(numericalList)):
        if target == numericalList[index]:
            locations.append(index)
    
    return locations

def lastSighting(targetLocations):
    lastLocation = targetLocations[len(targetLocations) - 1]
    return lastLocation

#Goal is to find last occurance of 1 (second index)
def main():
    target = 3
    numericalList = [1,3,4,9,8,3,0]

    targetLocations = everySighting(numericalList, target)
    if len(targetLocations) != 0:
        lastOccurance = lastSighting(targetLocations)
        print("Target locations:")
        print(targetLocations)
        print()
        print("Last occurance:")
        print(lastOccurance)
    else:
        print("The target is NOT in the list!")

main()