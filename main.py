from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import serial
import os
import threading
 
ESCAPE = '\033'
 
window = 0
 
#rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

anglePhalange1 = 0
anglePhalange2 = 0
anglePhalange3 = 0
 
DIRECTION = 1
 
 
def InitGL(Width, Height): 
 
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0) 
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)   
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
 
def keyPressed(*args):
	if args[0] == ESCAPE:
		sys.exit()



def createCube(scale = 1, scaleX = 1, scaleY = 1, scaleZ = 1):
	    # Draw Cube (multiple quads)
	glBegin(GL_QUADS)
	glColor3f(1.0,0.0,0.0)
	glVertex3d(scaleX * scale  , scaleY * scale  , scaleZ * scale)
	glVertex3d(scaleX * scale  , scaleY * scale  , -scaleZ * scale)
	glVertex3d(-scaleX * scale  , scaleY * scale  , -scaleZ * scale)
	glVertex3d(-scaleX * scale  , scaleY * scale  , scaleZ * scale)

	glColor3f(0.0,1.0,0.0)
	glVertex3d(scaleX * scale  , -scaleY * scale  , scaleZ * scale)
	glVertex3d(scaleX * scale  , -scaleY * scale  , -scaleZ * scale)
	glVertex3d(scaleX * scale  , scaleY * scale  , -scaleZ * scale)
	glVertex3d(scaleX * scale  , scaleY * scale  , scaleZ * scale)

	glColor3f(0.0,0.0,1.0)
	glVertex3d(-scaleX * scale  , -scaleY * scale  , scaleZ * scale)
	glVertex3d(-scaleX * scale  , -scaleY * scale  , -scaleZ * scale)
	glVertex3d(scaleX * scale  , -scaleY * scale  , -scaleZ * scale)
	glVertex3d(scaleX * scale  , -scaleY * scale  , scaleZ * scale)

	glColor3f(1.0,1.0,0.0)
	glVertex3d(-scaleX * scale  , scaleY * scale  , scaleZ * scale)
	glVertex3d(-scaleX * scale  , scaleY * scale  , -scaleZ * scale)
	glVertex3d(-scaleX * scale  , -scaleY * scale  , -scaleZ * scale)
	glVertex3d(-scaleX * scale  , -scaleY * scale  , scaleZ * scale)

	glColor3f(1.0,0.0,1.0)
	glVertex3d(scaleX * scale  , scaleY * scale  , -scaleZ * scale)
	glVertex3d(scaleX * scale  , -scaleY * scale  , -scaleZ * scale)
	glVertex3d(-scaleX * scale  , -scaleY * scale  , -scaleZ * scale)
	glVertex3d(-scaleX * scale  , scaleY * scale  , -scaleZ * scale)

	glColor3f(1.0,1.0,1.0)
	glVertex3d(scaleX * scale  , -scaleY * scale  , scaleZ * scale)
	glVertex3d(scaleX * scale  , scaleY * scale  , scaleZ * scale)
	glVertex3d(-scaleX * scale  , scaleY * scale  , scaleZ * scale)
	glVertex3d(-scaleX * scale  , -scaleY * scale  , scaleZ * scale)
	glEnd()


def finger(firstAngel, secondAngel, thirdAngel, hight):
	glRotatef(firstAngel, 1, 0, 0)
	createCube(1, 0.13, 0.2, hight)
	glRotatef(secondAngel, 1, 0, 0)
	glTranslatef(0, 0, hight*2)
	createCube(1, 0.13, 0.2, hight)
	glRotatef(thirdAngel, 1, 0, 0)
	glTranslatef(0, 0, hight*2)
	createCube(1, 0.13, 0.2, hight)
	#reste Angle
	glTranslatef(0, 0, hight*2*2*-1)
	glRotatef((firstAngel+secondAngel+thirdAngel)*-1, 1, 0, 0)
	
 
 
def DrawGLScene():
	global X_AXIS,Y_AXIS,Z_AXIS
	global DIRECTION

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glLoadIdentity()
	glTranslatef(0.0,0.0,-6.0)

	glRotatef(X_AXIS,1.0,0.0,0.0)
	glRotatef(Y_AXIS,0.0,1.0,0.0)
	glRotatef(Z_AXIS,0.0,0.0,1.0)

	createCube(1, 0.7, 0.3)

	glTranslatef(0.7 - 0.13, 0, 1.3)
	finger(20,20,20,.3)
	glTranslatef(-0.30, 0, 0)
	finger(0,0,0,.3)
	glTranslatef(-0.30, 0, 0)
	finger(0,0,0,.3)
	glTranslatef(-0.30, 0, 0)
	finger(10,10,10,.3)
	glTranslatef(-0.30, 0, 0)
	finger(0,10,20,.2)

	X_AXIS = X_AXIS + .30
	#Y_AXIS = Y_AXIS + .3
	Z_AXIS = Z_AXIS + .3

	glutSwapBuffers()
 
 
 
def main():
 
        global window
 
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640,480)
        glutInitWindowPosition(200,200)

        window = glutCreateWindow('OpenGL Python Hand')
 
        glutDisplayFunc(DrawGLScene)
        glutIdleFunc(DrawGLScene)
        glutKeyboardFunc(keyPressed)
        InitGL(640, 480)
        glutMainLoop()
 
if __name__ == "__main__":
        main() 