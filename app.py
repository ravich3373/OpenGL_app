from OpenGL.GL  import *
from OpenGL.GLUT import *
from OpenGL.GLU  import *
import numpy as np

print("how to make VIP evaluation app?")

window = 0                                             # glut window number
width, height = 500, 400                               # window size
x_pos,y_pos,x_inc,y_inc = 10,10,1,1

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

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    
    # ToDo draw rectangle
    global x_pos,y_pos,x_inc,y_inc
    x_sz,y_sz = 100,100
    if(x_pos > width-x_sz):
        x_inc = -1
    if(x_pos < 0):
        x_inc = 1
    if(y_pos > height-y_sz):
        y_inc = -1
    if(y_pos < 0):
        y_inc = 1
    refresh2d(width, height)
    glColor3f(1,1,1)

    glTranslate(x_pos,y_pos,0)
    #glRotate(x_pos,0,0,1)
    #draw_rect(0,0,x_sz,y_sz)
    draw_circle(0+1,0+1,10,50)
    #glTranslatef(5,5,5)
    x_pos += x_inc
    y_pos += y_inc
    glutSwapBuffers()                                  # important for double buffering
    

# initialization
print(bool(glutInit))
if(bool(glutInit)):
    glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("VIP_evaluations app")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()