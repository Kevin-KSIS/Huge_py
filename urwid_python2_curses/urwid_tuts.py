import urwid

def show_or_exit(key):
    if key in ('q','Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

txt  = urwid.Text(u"Hello World of curses interface!\n", align='center')
fill = urwid.Filler(txt, 'middle')
loop = urwid.MainLoop(fill, unhandled_input = show_or_exit)
loop.run()

