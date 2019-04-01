from math import *

import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def r(x):
    return x/255

def g(x):
    return x/255

def b(x):
    return x/255
def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,40)   # mn extension l perspective bta3 l ragl l labs azra2
    gluLookAt(3,7,10,
              0,0,0,
              0,1,0)

    glClearColor (1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)




def house1 (x,y,z):
    glLoadIdentity()
    glColor3f(x,y,z)
    glTranslate(-13,0,-10)
    glutSolidCube(10)
    glLoadIdentity()
    glRotate(90,0,1,0)
    glColor3f(r(9),g(134),b(135))
    glBegin(GL_QUADS)
    glVertex(1,-.2,-3.6)
    glVertex(3,-.2,-3.6)
    glVertex(3,4,-3.6)
    glVertex(1,4,-3.6)
    glEnd()

'''def house2 (x,y,z):
    glColor3f(x,y,z)
    glRotate(90,0,1,0)
    glTranslate(-15,0,-20)
    glutSolidCube(10)
    glLoadIdentity()
    glRotate(90,0,1,0)
    glColor3f(r(9),g(134),b(135))
    glTranslate(-11,0,0)
    glBegin(GL_QUADS)
    glVertex(2,-.2,-5)
    glVertex(4,-.2,-5)
    glVertex(4,4,-5)
    glVertex(2,4,-5)
    glEnd()
    glLoadIdentity()'''



def Tree(x,y,z):
    glColor3f(r(188),g(94),b(16))
    glRotate(90,0,1,0)
    glTranslate(x+.05,y-3,z+.5)
    glScale(.1,1,.1)
    glutSolidCube(6)
    glLoadIdentity()
    glColor3f(r(148),g(239),b(79))
    glRotate(90,0,1,0)
    glTranslate(x,y,z)
    glutSolidSphere(1.5,15,15)
    glLoadIdentity()


def road ():
    glLoadIdentity()
    glColor3f(r(51),g(52),b(53))
    glRotate(90,0,1,0)
    glBegin(GL_POLYGON)
    glVertex(20,0,3)
    glVertex(20,0,-3)
    glVertex(-15,0,-3)
    glVertex(-15,0,3)
    glEnd()
    glLoadIdentity()


def xyz():

    glColor3f(1,0,0)
    glBegin(GL_LINES)
    glVertex(0,0,0)
    glVertex(10,0,0)

    glColor3f(0,1,0)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)

    glColor3f(0,0,1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()


angle = 0
x=0
right = True

def draw ():
    global angle
    global x
    global right
    glClearColor(r(193),g(204),b(211),0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    road()



    house1(r(158),g(154),b(144)) 


    #b3ed ymyn
    glColor3f(r(75),g(72),b(72))
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(-.5*5+x,-.5*.25*5,-.25*5)
    glRotate(angle,0,0,1)  # angle , vector l dwran
    glutSolidTorus(.125,.5,5,10)
    #oryb ymyn
    glColor3f(r(75),g(72),b(72))
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(.5*5+x,-.5*.25*5,-.25*5)
    glRotate(angle,0,0,1)  # angle , vector l dwran
    glutSolidTorus(.125,.5,5,10)


    glLoadIdentity()
    glColor3f(r(176),g(21),b(21))
    glRotate(90,0,1,0)
    glTranslate(x,0,0)
    glScale(1,.25,.5)
    glutSolidCube(5)

    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(x,.25*5,0)
    glScale(.5,.25,.5)
    glutSolidCube(5)

    #oryb shmal
    glLoadIdentity()
    glColor3f(r(75),g(72),b(72))
    glRotate(90,0,1,0)
    glTranslate(.5*5+x,-.5*.25*5,.25*5)
    glRotate(angle,0,0,1)  # angle , vector l dwran
    glutSolidTorus(.125,.5,5,10)
    glLoadIdentity()


    #b3ed shmal
    glLoadIdentity()
    glColor3f(r(75),g(72),b(72))
    glRotate(90,0,1,0)
    glTranslate(-.5*5+x,-.5*.25*5,.25*5)
    glRotate(angle,0,0,1)  # angle , vector l dwran
    glutSolidTorus(.125,.5,5,10)
    glLoadIdentity()

    glLoadIdentity()
    glColor3f(r(66),g(134),b(244))
    glRotate(90,0,1,0)
    glTranslate(-x, 0, z)
    glRotate(angle, 1, 0, 0)
    glutSolidSphere(1.5,20,20)
    glLoadIdentity()
    Tree(4,3,3)
    Tree(-4,3,3)

    glutSwapBuffers()
    if(x<5 and right):
        x+=.001
        angle-=.1
    else :
        right = False
    if (x>-7 and right==False):
        x-=.001
        angle+=.1
    else :
        right =True

z=0
def specialKeyHandler(key , x,y): 
    global z 
    if key == GLUT_KEY_RIGHT :     # mt5zn hna kol l special keys 
        z=z+.2
    elif key== GLUT_KEY_LEFT:
        z=z-.2
    draw ()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(specialKeyHandler)
glutMainLoop()