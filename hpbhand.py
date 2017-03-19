import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
	gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

	#Camera zoom
	glTranlate(0.0, 0.0, -10)

	while True:
		pass

class Palm:
	pass

class Finger:
	pass

class Hand:
	pass

