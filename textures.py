import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
import matplotlib.pyplot as plt

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


#Settings
width = 852
height = 480
resolution = (width,height)
#texture_data = np.random.randint(256,size=(height, width, 3))
texture_data = plt.imread('pics/1.jpg')
print(texture_data.shape)
print(type(texture_data))
#pygame init
pygame.init()
gameDisplay = pygame.display.set_mode(resolution,OPENGL)

#OpenGL init
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0,resolution[0],0,resolution[1],-1,1)
glMatrixMode(GL_MODELVIEW)
glDisable(GL_DEPTH_TEST)
glClearColor(0.0,0.0,0.0,0.0)
glEnable(GL_TEXTURE_2D)

#Set texture
texture = glGenTextures(1)
glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
glBindTexture(GL_TEXTURE_2D, texture)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
glGenerateMipmap(GL_TEXTURE_2D)

glActiveTexture(GL_TEXTURE0)

#Clean start
glClear(GL_COLOR_BUFFER_BIT)
glLoadIdentity()

#draw rectangle
#glTranslatef(300,200,0)
#glBegin(GL_QUADS)
#glVertex2f(0,0)
#glVertex2f(0,height)
#glVertex2f(width,height)
#glVertex2f(width,0)
#glEnd()
#glFlush()
#draw rectangle

#glTranslatef(300,200,0)
glBegin(GL_QUADS)

glTexCoord(0,0)
glVertex2f(0,0)

glTexCoord(0,1)
glVertex2f(0,height)

glTexCoord(1,1)
glVertex2f(width,height)

glTexCoord(1,0)
glVertex2f(width,0)

glEnd()
glFlush()
refresh2d(width,height)
draw_rect(0,0,50,50)

#game loop until exit
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    #throttle
    pygame.time.wait(100)