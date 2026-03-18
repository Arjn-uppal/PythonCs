class vector:

    def __init__(vector, m, d):
        error = False
        d = d.upper()

        if m > 0:
            vector.magnitude = m

            if d == "RIGHT":
                vector.direction = "RIGHT"

            elif d == "LEFT":
                vector.direction = "LEFT"

            else:
                error = True

        else:
            error = True

        if error:
            print("ERROR IN INPUT: SO I CREATED A VECTOR 1 UNIT [RIGHT]")
            vector.direction = "RIGHT"
            vector.magnitude = 1
            vector.vectorSize = 1


    def add(vector, v):
        sum = vector.vectorSize + v.vectorSize
        if sum > 0:
            return Vector(sum, "RIGHT")
        else:
            return Vector(-1 * sum, "LEFT")
        

    def subtract(vector, v):
        diff = vector.vectorSize - v.vectorSize
        if diff > 0:
            return Vector(diff, "RIGHT")
        else:
            return Vector(-1 * diff, "LEFT")
        

    def __str__(vector):
        return "The resultant vector is: " + str(vector.magnitude) + " " + "[" + vector.direction + "]"
    
