import pygame
import random
from pygameRilett import Game
from pygameRilett import Room
from pygameRilett import TextRectangle
from pygameRilett import Alarm

#Create a new Game
g = Game(640,480)

#Graphic Resources
BLACK = (0,0,0)
WHITE = (255,255,255)
myFont = g.makeFont("Arial",38)
gameBackground = g.makeBackground(BLACK)


#Button for the first room -&gt; Sends game to next room
class NextRoomButton(TextRectangle):

	def __init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor):
		TextRectangle.__init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)

	def update(self):
		# Check for a mouse click
		self.checkMousePressedOnMe(event)

		# Update Game State when mousebutton released
		if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:

			# Go to next room
			g.nextRoom()


			# Prevent multiple mouse clicks
			self.mouseHasPressedOnMe = False


#Button for the second room -&gt; Makes a random message appear every 1 second
class StartTimerButton(TextRectangle):

	def __init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor):
		TextRectangle.__init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)
		self.thingsToSay = ["Hi", "Bye", "Welcome", "Greetings", "Go Away", "See You Later", "Come Here"]

		#Create an Alarm
		self.timer = Alarm()

	def update(self):
		# Check for a mouse click
		self.checkMousePressedOnMe(event)

		# Update Game State when mousebutton released
		if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:

			#Set Timer To go off 2 seconds after button being clicked
			self.timer.setAlarm(2000)

			# Prevent multiple mouse clicks
			self.mouseHasPressedOnMe = False

		#Check if the alarm is done
		if self.timer.finished():

			#Change the word
			self.word = random.choice(self.thingsToSay)
			self.setText(self.word)

			#Reset the alarm to go off again after 1 second (Creates a little alarm loop constantly going off after 1 second
			self.timer.setAlarm(1000)
			

#Create the Rooms and add them to the game
r1 = Room("Level 1",gameBackground )
g.addRoom(r1)
r2 = Room("Level 2",gameBackground)
g.addRoom(r2)


#Create the buttons objects and add them to the rooms
myButton = NextRoomButton("Next Room",g.windowWidth/2-150/2, g.windowHeight - 75, myFont, BLACK, 200,50, WHITE)
myTimerStart = StartTimerButton("Start Timer",g.windowWidth/2-150/2, g.windowHeight - 75, myFont, BLACK, 200,50, WHITE)
r1.addObject(myButton)
r2.addObject(myTimerStart)


#Start Game----------------------------------------------------------
#Game Loop
g.start()

while g.running:

	# How often the game loop executes each second
	dt = g.clock.tick(60)

	# Check Events
	for event in pygame.event.get():

		# Check for [x]
		if event.type == pygame.QUIT:
			g.stop()

	# Update All objects in Room
	g.currentRoom().updateObjects()

	# Render Background to the game surface
	g.currentRoom().renderBackground(g)

	# Render ALL Objects to the game surface
	g.currentRoom().renderObjects(g)

	# Draw everything on the screen
	pygame.display.flip()

pygame.quit()