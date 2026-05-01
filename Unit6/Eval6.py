import pygame
from pygameRilett import Game
from pygameRilett import Room
from pygameRilett import GameObject

# Create a new game
# NOTE g is comprised of all the methods and global variables inside the Game class
g = Game(550,480)

# Color
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)

#Create Resources
simpleBackground = g.makeBackground(BLACK)

#NOTE "makeRectangle method is from the pygameRillet file"
rectangleImage = g.makeRectangle(g.windowWidth, 20, RED)
circleImage = g.makeCircle(10, WHITE)

marioImage = g.makeSpriteImage("marioPiic.png")

# Alter the size of the image to fit the game
marioImage = pygame.transform.scale(marioImage, (180,140))

# Create rooms
r1 = Room("Game", simpleBackground)
g.addRoom(r1)

# Game Object Classes
# NOTE we are extending the GameObject class in the pygame.rillet file which is the parameter for the Platform class

# NOTE that each class is inheriting the "Draw" method from the pygame.sprite.class in pygameRillet file. This happens
# through the extension of the GameObject class
class Platform(GameObject):

    def __init__(self, picture, xPos, yPos):

        GameObject.__init__(self, picture)
        self.rect.x = xPos
        self.rect.y = yPos

class Enemy(GameObject):
    def __init__(self, picture, xPos, yPos):

        GameObject.__init__(self, picture)
        self.rect.center = (xPos, yPos)

class Player(GameObject):
    def __init__(self, picture, xPos, yPos):

        GameObject.__init__(self, picture)
        self.rect.x = xPos
        self.rect.y = yPos
        self.image.set_colorkey(WHITE)

#Initialize Objects and add to the room
floor = Platform(rectangleImage, 0, 450)
r1.addObject(floor)

circleEnemy = Enemy(circleImage, g.windowWidth/2, 425)
r1.addObject(circleEnemy)

mario = Player(marioImage, 0, 350)
r1.addObject(mario)

#Initialize the game
g.start()

#Game Loop
while g.running:


    # Limit the game execution framerate
    dt = g.clock.tick(60)

    # Check for Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            g.stop()

    # Update the gamestate of all the objects
    g.currentRoom().updateObjects()

    # Render the background to the window surface
    g.currentRoom().renderBackground(g)

    # render the object images to the background
    g.currentRoom().renderObjects(g)

    # Draw everything on the screen
    pygame.display.flip()

pygame.quit()