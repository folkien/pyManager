#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import curses
import curses.textpad

class cCommandWindow:
		'Klasa opisująca okno polecen.'


		def __init__(self):
				# Wskazniki :
				self.winPtr = 0

				self.directory 	= "/"
				self.cursor 	= 0
				self.dispList 	= [ "../", "./" ]

				#polozenia okna i wymiary
				self.posx   = 0
				self.posy   = 0
				self.width  = 10
				self.height = 10

		def setWin(self,window):
				self.winPtr = window

		def moveCursor(self,direction):
				if (direction == 1):
						if (self.cursor < self.dispList):
								self.cursor += 1
				else:
						if (self.cursor > 0):
								self.cursor -= 1


		def readDirectory(self):
				self.dispList = [ f for f in os.listdir(self.directory) ]

		def paint(self):
				pos_start = 0
				if (self.cursor > self.height):
					pos_start = self.cursor - self.height

				#rysujemy okno
				self.winPtr.border(0)
				for i in range(0, min(len(self.dispList), self.height) ):
					self.winPtr.addstr(self.posy+i+1, self.posx+1, self.dispList[pos_start + i])
				self.winPtr.refresh()



