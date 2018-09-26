from OpenGL.GL  import *
from OpenGL.GLUT import *
from OpenGL.GLU  import *
import gc

import numpy as np
import matplotlib.pyplot as plt

#print("how to make VIP evaluation app?")

window = 0                                             # glut window number
width, height = 852, 480                               # window size
resolution = (width,height)
x_pos,y_pos,x_inc,y_inc = 10,10,1,1
texture_data = plt.imread('pics/1.jpg')
print(texture_data.shape)
print(type(texture_data))

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()

def draw_circle(x_c,y_c,radius,points):
    glBegin(GL_POLYGON)
    vertices = np.linspace(0,1,num=points)
    y = (radius * np.sin(2*np.pi*vertices)) + x_c
    x = (radius * np.cos(2*np.pi*vertices)) + y_c
    for x_,y_ in zip(x,y):
        glVertex2f(x_,y_)
    glEnd()

def set_bg():
    #glEnable(GL_TEXTURE_2D)
#
    #texture = glGenTextures(1)
    #glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    #glBindTexture(GL_TEXTURE_2D, texture)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    #glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    #glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    #glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    #glGenerateMipmap(GL_TEXTURE_2D)
#
    #glActiveTexture(GL_TEXTURE0)

    #Clean start
    glClear(GL_COLOR_BUFFER_BIT )
    glLoadIdentity()

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

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    
    # ToDo draw rectangle
    global x_pos,y_pos,x_inc,y_inc
    x_sz,y_sz = 25,25
    if(x_pos > width-x_sz):
        x_inc = -1 * x_inc
    if(x_pos < 0):
        x_inc = -1 * x_inc
    if(y_pos > height-y_sz):
        y_inc = -1 * y_inc
    if(y_pos < 0):
        y_inc = -1 * y_inc
    refresh2d(width, height)
    glColor3f(1,1,1)
    set_bg()

    glTranslate(x_pos,y_pos,0)
    #glRotate(x_pos,0,0,1)
    glColor3f(0,0,1)
    draw_rect(0,0,x_sz,y_sz)

    #draw_circle(0+1,0+1,0,50)
    #glTranslatef(5,5,5)
    x_pos += x_inc
    y_pos += y_inc
    glutSwapBuffers()                                  # important for double buffering
    

# initialization
if __name__ == '__main__':
    print(bool(glutInit))
    if(bool(glutInit)):
        glutInit()                                             # initialize glut

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("VIP_evaluations app")              # create window with title
        #start texture
    glEnable(GL_TEXTURE_2D)

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
    #end texture
    glutDisplayFunc(draw)                                  # set draw function callback
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()