import os
if os.path.exists('\\\LOULOU-COMP\\SharedDocs'):
    path1 = '\\\LOULOU-COMP\\SharedDocs'
else:
    path1 = 'C:\\Documents and Settings\\All Users\\Documents'
filetoopen = open(path1 + '\\lol.txt', 'r+')
num = input('1 or 2 ')
if num == 1:
    thing = 2
else:
    thing = 1

while 1:
    if str(filetoopen.readline()).startswith(str(thing)):
        print filetoopen.readline()
    else:
        y = raw_input('what do you want to send? ')
        filetoopen.write(str(num) + y)


