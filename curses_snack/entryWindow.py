import snack
from snack import *

screen  = SnackScreen()

ret = EntryWindow(screen, 'Title', 'My super agenda', ['name', 'lastname', 'age'])

screen.finish()
status = ret[0]

values = ret[1]

# OK or cancel

print "Pressed %s" % (status)

#print every simple item
for item in values:
    print item
screen = SnackScreen()

lbox = Listbox(height = 20, width = 30, returnExit =1 )
lbox.append("Fedora",1)
lbox.append("ubuntu",2)
lbox.append("archlinux",3)

grid = GridForm(screen, "Select your favorite distro", 1, 1)
grid.add(lbox, 0, 0)

result = grid.runOnce()

screen.finish()

if lbox.current()==1:
    print "Selected Fedora"
if lbox.current()==2:
    print "Selected Ubuntu"
if lbox.current()==3:
    print "Selected ArchLinux"

screen = SnackScreen()



screen.finish()
