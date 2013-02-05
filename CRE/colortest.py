#! /usr/bin/env python

from os import system

# function to setup drawing mode
def setup():
    system('tput sc')
    system('tput clear')
    system('tput bold')

# function to draw color strips rectangle
def draw(x,y):
    sb = ''
    sc = ''
    for i in xrange(8):
        sb = 'tput setab %d' %i
        system(sb)
        sc = 'tput cup %d %d' %(y, x)
        system(sc)
        sp = '| FLOSS at %d %d |' %(x, y)
        print(sp)
        y += 1

# function to restore original display mode
def restore():
    system('tput sgr0')
    system('tput rc')

setup()

# starting location for drawing
x = 30
y = 12

# draw 3 sets of color strips rectangles
for i in xrange(3):
    for j in xrange(3):
        draw(x, y)
        x += 5
        y += 5
    x += 15
    y  = 12

restore()
