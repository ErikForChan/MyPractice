import curses
myscreen = curses.initscr()
myscreen.border(0)
myscreen.addstr("123")
# myscreen.addstr(1, 14, "Python curses in action!")
myscreen.refresh()
myscreen.getch()