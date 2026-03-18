class Vector:

    def __init__(vector, m, d):
        error = False
        d = d.upper()

        if m > 0:
            vector.magnitude = m

            if d == "RIGHT":
                vector.direction = "RIGHT"
                vector.vectorSize = m

            elif d == "LEFT":
                vector.direction = "LEFT"
                vector.vectorSize = m * -1

            else:
                error = True

        else:
            error = True

        if error:
            print("ERROR IN INPUT: SO I CREATED A VECTOR 1 UNIT [RIGHT]")
            vector.direction = "RIGHT"
            vector.magnitude = 1
            vector.vectorSize = 1


    def add(vector, amount):
        sum = vector.vectorSize + amount.vectorSize
        if sum > 0:
            return Vector(sum, "RIGHT")
        else:
            return Vector(-1 * sum, "LEFT")
        

    def subtract(vector, amount):

        #we do "amount.vectorSize" because you cannot perform a mathematical operation
        #With both a scalar (vector.vectorSize) and a vector (amount variable)
        diff = vector.vectorSize - amount.vectorSize
        if diff > 0:
            return Vector(diff, "RIGHT")
        else:
            return Vector(-1 * diff, "LEFT")
        

    def __str__(vector):
        return str(vector.magnitude) + " " + "[" + vector.direction + "]"
    

def main():
    #Create some vectors
    v1 = Vector(5, "RIGHT")
    v2 = Vector(10, "RIGHT")
    v3 = Vector(6, "LEFT")

    #Add v1 and v2
    a = v1.add(v2)
    print(v1, "+", v2, "=", a)

    #Subtract v1 from v2
    b = v2.subtract(v1)
    print(v2, "-", v1, "=", b)

    #Add v1 and v3
    c = v1.add(v3)
    print(v1, "+", v3, "=", c)


main()