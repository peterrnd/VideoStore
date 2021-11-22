"""
Program: videostoreGUI.py
Author: Peter Rand 11/17/2021
Simple demo of fictitious video rental store.
*** NOTE: the file "breezypythongui.py" MUST be in the same directory as the file for the application to work.***
**** NOTE: NEED IMAGE FILE: "Hollywoodvideo_logo.png". MUST be in the same directory as the file for the application to work.***
*** NOTE: Need to have mp3 file: "sound-effects-library-cash-register-sound.mp3". MUST be in the same directory as the file for the application to work.***
*** NOTE: MUST install the pygame package by running: pip install pygame
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
import pygame

class VideoStoreGUI(EasyFrame):
	

	def __init__(self):

		"""Sets the window and the widgets."""
		EasyFrame.__init__(self, title = "HOLLYWOOD VIDEO ONLINE RENTAL STORE", width = 450, height = 500, background = "#3d02bd", resizable = False)
		# Logo Image
		self.imageLabel = self.addLabel(text = "", row = 0, column = 0, columnspan = 2, background = "#5203fc")
		# Load the image and associate it with the image label
		self.image = PhotoImage(file = "Hollywoodvideo_logo.png")
		self.imageLabel["image"] = self.image

		# change font family
		font = Font(family = "arial", size = 12, weight = "bold")

		# add labels to window
		self.textLabel1 = self.addLabel(text = "Number of *NEW* video rentals at $3.99 each:", row = 1, column = 0, font = font, background = "#3d02bd", foreground = "white")
		self.textLabel2 = self.addLabel(text = "Number of *OLD* videos rentals at $2.50 each:", row = 2, column = 0, font = font, background = "#3d02bd", foreground = "white")
		self.textLabel3 = self.addLabel(text = "Total Amount Due is:", row = 3, column = 0, font = font, background = "#3d02bd", foreground = "white")
		# add input fields to window
		self.inputField1 = self.addIntegerField(value = 0, row = 1, column = 1)
		self.inputField2 = self.addIntegerField(value = 0, row = 2, column = 1)
		# add Total Amount Due output field
		self.outputField = self.addFloatField(value = 0.0, row = 3, column = 1, width = 10, state = "readonly")
		# add Calculate Total button to window
		self.addButton(text = "Calculate Total", row = 4, column = 0, columnspan = 2, command = self.calculate)
		
	# Event handler
	def calculate(self):
		# adding the sound to button
		pygame.mixer.init()
		pygame.mixer.music.load("sound-effects-library-cash-register-sound.mp3")
		pygame.mixer.music.play(loops = 0)
		# local variables to calculate() function
		newRental = self.inputField1.getNumber()
		oldRental = self.inputField2.getNumber()
		newCost = 3.99
		oldCost = 2.50

		# calculation
		calcTotal = (newCost * newRental) + (oldCost * oldRental)
		result = "$" + ("%10.2f" % calcTotal)

		self.outputField.setValue(result)

# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	VideoStoreGUI().mainloop()

# global call to trigger the main() function
if __name__ == "__main__":
	main()