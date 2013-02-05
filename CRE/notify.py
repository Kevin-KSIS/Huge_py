#!/usr/bin/python2

import pygtk
pygtk.require('2.0')
import pynotify
import sys

if __name__ == '__main__':
    if not pynotify.init("Basics"):
        sys.exit(1)

    n = pynotify.Notification("New HF MSG", "From some user")

    if not n.show():
        print "Failed to send notification"
        sys.exit(1)


