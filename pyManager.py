#!/usr/bin/env python
 
import curses
import curses.textpad
import time, os

# At start : Get actual directory
# TODO : Reading last configuration.


# userinterface.py
# Do zarządzania oknami


# CommandWindow.py
# Dodać klasę odpowiedzialną za okno aplikacji.
# Klasa ta musi posiadać katalog WORKDIR
# zmienna - pozycja kursora w WORKDIR
# zmienna - lista plików pobrana z WORKDIR
# metoda wyświetlająca WORKDIR.
# metoda ktora porusza kursorem
# metoda refreshDirectory, aktualizuje liste plikow.
# metoda repaint - rysuje 
# metoda resize


directory = os.getcwd()

#pliki z danego katalogu
files = [ f for f in listdir(directory) ]

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(1)
 

leftwin = screen.subwin(30,50,0,0)
leftwin.border(0)
leftwin.refresh()
rightwin = screen.subwin(30,50,0,51)
rightwin.border(0)
rightwin2.refresh()


x = 'a'
while (x != 120) :
	x = screen.getch()

#"Zamykam system."
time.sleep(1)
curses.nocbreak(); 
screen.keypad(0); 
curses.echo()
curses.endwin() 
