import pygame
import random
from pygameRilett import Game
from pygameRilett import Room
from pygameRilett import TextRectangle
from pygameRilett import GameObject


# Create a new game
# NOTE g is comprised of all the methods and global variables inside the Game class
g = Game(800,600)

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# Create Resources --> Images, Fonts, Backgrounds
gameFont = g.makeFont("Arial", 38)
gameBackground = g.makeBackground(BLACK)

diamondPics = []
for i in range(2, 15):
    diamondPics.append(g.makeSpriteImage("cards\DIAMONDS" + str(i) + ".jpg"))

heartPics = []
for i in range(2, 15):
    heartPics.append(g.makeSpriteImage("cards\HEARTS" + str(i) + ".jpg"))

spadePics = []
for i in range(2, 15):
    spadePics.append(g.makeSpriteImage("cards\SPADES" + str(i) + ".jpg"))

clubPics = []
for i in range(2, 15):
    clubPics.append(g.makeSpriteImage("cards\CLUBS" + str(i) + ".jpg"))

topCard = g.makeSpriteImage("cards\TOP.jpg")

# Create rooms and add them to the game
r1 = Room("Game", gameBackground)
g.addRoom(r1)

# Game Object Classes
# NOTE we are extending the GameObject class in the pygame.rillet file which is the parameter for the Platform class

# NOTE that each class is inheriting the "Draw" method from the pygame.sprite.class in pygameRillet file. This happens
# through the extension of the GameObject class

# Classes for Game Objects---------------------------------------
class Card(GameObject):

    def __init__(self, picture, value, suit):

        # Initialize the super class
        GameObject.__init__(self, picture)

        # Attributes
        self.value = value # 2 - 14
        self.suit = suit # H, D, S, C

    def __str__(self):
        return str(self.value) + self.suit
    

class CardDeck(GameObject):

    def __init__(self, picture, xPos, yPos):

        # Initialize the super class
        GameObject.__init__(self, picture)

        # Attributes
        self.deck = []
        self.rect.x = xPos
        self.rect.y = yPos

        for i in range(0, len(diamondPics)):
            self.deck.append(Card(diamondPics[i], i+2, "D"))

        for i in range(0, len(heartPics)):
            self.deck.append(Card(heartPics[i], i+2, "H"))

        for i in range(0, len(spadePics)):
            self.deck.append(Card(spadePics[i], i+2, "S"))

        for i in range(0, len(clubPics)):
            self.deck.append(Card(clubPics[i], i+2, "C"))

        random.shuffle(self.deck)

    def __str__(self):
        
        s = ""
        for card in self.deck:
            s = s + str(card) + " "
        s = "Deck:\n" + s + "\n"
        return s


#Initialize Objects in the Room------------------------------------
playerHandLabel = TextRectangle("Players Hand - Click Card To Play", 8, 0, gameFont, RED)
deckLabel = TextRectangle("Deck - Click Card To Deal", 8, 200, gameFont, RED)
playedLabel = TextRectangle("Played Cards", 8, 400, gameFont, RED)

r1.addObject(playerHandLabel)
r1.addObject(deckLabel)
r1.addObject(playedLabel)

d = CardDeck(topCard, 8, 250)
r1.addObject(d)
print(d)

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