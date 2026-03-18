class Robot:

    def __init__(robot, position, direction):
        if direction == "RIGHT":
            robot.position = position
        
        elif direction == "LEFT":
            robot.position = -1 * position

        else:
            print("Invalid direction, POSITION = HOME BASE")
            robot.position = 0

        robot.speed = 0

    
    def changeSpeed(robot, amount):
        if robot.speed + amount < 0:
            robot.speed = 0
        
        elif robot.speed + amount > 30:
            robot.speed = 30
        
        else:
            robot.speed = robot.speed + amount


    def moveRight(robot, time):
        if robot.speed == 0:
            print("Set Speed Before Moving")
        else:
            robot.position = robot.position + robot.speed * time


    def moveLeft(robot, time):
        if robot.speed == 0:
            print("Set Speed Before Moving")
        else:
            robot.position = robot.position - robot.speed * time



    def __str__(robot):
        if robot.position == 0:
            return "At Home Base"
        
        elif robot.position > 0:
            return "Final Position is: " + str(robot.position) + "cm RIGHT of Home Base"
        
        else:
            if robot.position < 0:
                robot.position = -1 * robot.position
            return "Final Position is: " + str(robot.position) + "cm LEFT of Home Base"
        

def main():
    #Create robot 60 cm right of his home base
    robot1 = Robot(60, "RIGHT")

    #Move right at 5 cm/s for 10s
    robot1.changeSpeed(5)
    robot1.moveRight(10)

    #Slow down by 2 cm/s and keep moving right for 5s
    robot1.changeSpeed(-2)
    robot1.moveRight(5)

    #Turn around and move left speeding up by 6 cm/s for 12s
    robot1.changeSpeed(8)
    robot1.moveLeft(12)

    #Display final position
    print(robot1)

main()