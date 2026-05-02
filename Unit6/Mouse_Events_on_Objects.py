import random
import pygame

from pygameRilett import Game
from pygameRilett import Room
from pygameRilett import GameObject

# Create a new game
# NOTE g is comprised of all the methods and global variables inside the Game class
g = Game(550,480)

# Color
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)


# Create Resources
simpleBackground = g.makeBackground(BLACK)
whiteCircleImage = g.makeCircle(60, WHITE)
blueCircleImage = g.makeCircle(60, BLUE)
greenRectangleImage = g.makeRectangle(50, 50, GREEN)

# Create rooms
r1 = Room("Game", simpleBackground)
g.addRoom(r1)

# Game Object Classes
# NOTE we are extending the GameObject class in the pygame.rillet file which is the parameter for the Platform class

# NOTE that each class is inheriting the "Draw" method from the pygame.sprite.class in pygameRillet file. This happens
# through the extension of the GameObject class

# Change color when clicked
class Circle(GameObject):
    def __init__(self, picture, xPos, yPos):

        GameObject.__init__(self, picture)
        self.rect.center = (xPos, yPos)

    # Update game State based on input states
    # This is for FPS and it will check if an event has happened for every frame
    def update(self):
        self.checkMousePressedOnMe(event)

        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
            self.image = blueCircleImage
            self.mouseHasPressedOnMe = False

# Dragable Object
class Rectangle(GameObject):
    def __init__(self, picture, xPos, yPos):

        GameObject.__init__(self, picture)
        self.rect.x = xPos
        self.rect.y = yPos

    # Update game State based on input states
    # This is for FPS and it will check if an event has happened for every frame
    def update(self):

        self.checkMousePressedOnMe(event)

        if self.mouseHasPressedOnMe:

            self.rect.center = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseHasPressedOnMe = False



#Initialize Objects and add to the room
for i in range(0, 5):
    x = random.randint(0, g.windowWidth)
    y = random.randint(0, g.windowHeight)
    c = Circle(whiteCircleImage, x, y)
    r1.addObject(c)

for i in range(0, 5):
    x = random.randint(0, g.windowWidth)
    y = random.randint(0, g.windowHeight)
    r = Rectangle(greenRectangleImage, x, y)
    r1.addObject(r)


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