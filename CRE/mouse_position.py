from Xlib import display
from time import sleep
import random

random_x = random.randint(0,1366)
random_y = random.randint(0,768)

while 1:
    print "Gx: "+str(random_x)+" Gy: "+str(random_y)
    print "x: " +str( display.Display().screen().root.query_pointer()._data['root_x'])+" y: "+ str(display.Display().screen().root.query_pointer()._data['root_y'])
    if display.Display().screen().root.query_pointer()._data['root_x']==random_x and display.Display().screen().root.query_pointer()._data['root_y']==random_y:
        exit(0)
