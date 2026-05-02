import random
import pygame

from pygameRilett import Game
from pygameRilett import Room
from pygameRilett import GameObject
from pygameRilett import TextRectangle

# Create a new game
# NOTE g is comprised of all the methods and global variables inside the Game class
g = Game(640,480)

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)


# Create Resources
simpleBackground = g.makeBackground(BLACK)
gameFont = g.makeFont("Arial", 38)

# Create rooms
r1 = Room("Game", simpleBackground)
g.addRoom(r1)

# Game Object Classes
# NOTE we are extending the GameObject class in the pygame.rillet file which is the parameter for the Platform class

# NOTE that each class is inheriting the "Draw" method from the pygame.sprite.class in pygameRillet file. This happens
# through the extension of the GameObject class

# Classes for Game Objects
class ClickButton(TextRectangle):

    def __init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor):
        TextRectangle.__init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)

        self.clickCounter = 0

    def update(self):

        self.checkMousePressedOnMe(event)

        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:

            self.clickCounter += 1
            clickedTimes.setText("You Clicked: " + str(self.clickCounter) + " Times")

            self.mouseHasPressedOnMe = False

#Initialize Objects and add to the room
title = TextRectangle("CLICK COUNTER", 10, 10, gameFont, WHITE)
r1.addObject(title)

b = ClickButton("CLICK ME", 10, g.windowHeight - 75, gameFont, BLACK, 150, 40, WHITE)
r1.addObject(b)

clickedTimes = TextRectangle("You Clicked: " + str(b.clickCounter) + " Times", 10, 50, gameFont, WHITE)
r1.addObject(clickedTimes)

# Start Game
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