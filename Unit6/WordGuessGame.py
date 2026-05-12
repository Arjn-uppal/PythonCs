import pygame

from pygameRilett import Game
from pygameRilett import Room
from pygameRilett import TextRectangle
from pygameRilett import TextCircle
from pygameRilett import GameObject

# Create a new game
# NOTE g is comprised of all the methods and global variables inside the Game class
g = Game(800,600)

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)


# Create Resources
gameBackground = g.makeBackground(BLUE)
titleFont = g.makeFont("Arial", 38)

# Create rooms
r1 = Room("Start Menu", gameBackground)
g.addRoom(r1)

r2 = Room("Word Game", gameBackground)
g.addRoom(r2)

# Game Object Classes
# NOTE we are extending the GameObject class in the pygame.rillet file which is the parameter for the Platform class

# NOTE that each class is inheriting the "Draw" method from the pygame.sprite.class in pygameRillet file. This happens
# through the extension of the GameObject class

# Classes for Game Objects---------------------------------------
class StartButton(TextRectangle):

    def __init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor):
        TextRectangle.__init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)

    def update(self):

        self.checkMousePressedOnMe(event)

        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:

            # Go to next room
            g.nextRoom()

            # Prevent multiple mouse clicks
            self.mouseHasPressedOnMe = False


class ChoiceLetter(TextCircle):

    def __init__(self, text, xCenter, yCenter, font, textColor, buttonRadius, buttonColor):
        TextCircle.__init__(self, text, xCenter, yCenter, font, textColor, buttonRadius, buttonColor)

        self.letter = text


class MysteryLetter(TextCircle):

    def __init__(self, text, correctLetter, xCenter, yCenter, font, textColor, buttonRadius, buttonColor):
        TextCircle.__init__(self, text, xCenter, yCenter, font, textColor, buttonRadius, buttonColor)

        self.correctLetter = correctLetter


class MysteryWord(GameObject):

    def __init__(self, word, xPos, yPos, guesses):
        GameObject.__init__(self)


        #Attributes
        self.mysteryWord = word
        self.letters = []

        for i in range(0, len(self.mysteryWord)):
            letter = MysteryLetter("-", self.mysteryWord[i], 70 * (i*1) + xPos, yPos, titleFont, BLACK, 25, WHITE)
            self.letters.append(letter)
            r2.addObject(letter)


#Initialize Objects in the Room------------------------------------
title = TextRectangle("Guess a Word Game", g.windowWidth/2 - 150, 100, titleFont, WHITE)
r1.addObject(title)

start = StartButton("START", g.windowWidth/2 - 75, 325, titleFont, BLACK, 150, 50, WHITE)
r1.addObject(start)

mw = MysteryWord("GLENDALE", 15, 500, 5)
r2.addObject(mw)


charactersRow1 = "ABCDEFGHIJ"
for i in range(0, len(charactersRow1)):
    l = ChoiceLetter(charactersRow1[i], (70)*(i+1) + 15, 40, titleFont, BLACK, 25, WHITE)
    r2.addObject(l)

charactersRow2 = "KLMNOPQRST"
for i in range(0, len(charactersRow2)):
    l = ChoiceLetter(charactersRow2[i], (70)*(i+1) + 15, 120, titleFont, BLACK, 25, WHITE)
    r2.addObject(l)

charactersRow3 = "UVWXYZ"
for i in range(0, len(charactersRow3)):
    l = ChoiceLetter(charactersRow3[i], (70)*(i+1) + 15, 200, titleFont, BLACK, 25, WHITE)
    r2.addObject(l)


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