import curses

# initialize curses
stdscr = curses.initscr()
# Must be called if the programmer wants to use colors, and before any other color manipulation routine is called. It is good practice to call this routine right after initscr().
curses.start_color()


# Usually curses applications turn off automatic echoing of keys to the screen, in order to be able to read keys and only display them under certain circumstances. This requires calling the noecho() function.
curses.noecho()

# Applications will also commonly need to react to keys instantly, without requiring the Enter key to be pressed; this is called cbreak mode, as opposed to the usual buffered input mode.
curses.cbreak()

# Terminals usually return special keys, such as the cursor keys or navigation keys such as Page Up and Home, as a multibyte escape sequence. While you could write your application to expect such sequences and process them accordingly, curses can do it for you, returning a special value such as curses.KEY_LEFT. To get curses to do the job, you’ll have to enable keypad mode.
stdscr.keypad(True)



# produce a beep sound
curses.beep()

# set cursor visibility. 0 hidden, 1 underline, 2 block
curses.curs_set(2)

# sleep program (miliseconds)
curses.napms(10)

# delays console output (miliseconds)
curses.delay_output(10)

# clear the input
curses.flushinp()

# Return the current coordinates of the virtual screen cursor as a tuple (y, x)
curses.getsyx()


# if default terminal colors could be changed, you can change them with curses.init_color(colorid,r,g,b)
if curses.can_change_color():
  colornumber = 0
  r,g,b = 0,0,0
  curses.init_color(colornumber,r,g,b)


# Resize the standard and current windows to the specified dimensions
# curses.resizeterm(100,300)

# Return a bytes object containing the terminfo long name field describing the current terminal.
curses.longname()





# If flag is False, the effect is the same as calling noqiflush(). If flag is True, or no argument is provided, the queues will be flushed when these control characters are read.
curses.qiflush(True)

# Save the current state of the terminal modes in a buffer, usable by resetty().
curses.savetty()
# Restore the state of the terminal modes to what it was at the last call to savetty().
curses.resetty()


# Sets the number of columns used by the curses library when converting a tab character to spaces as it adds the tab to a window.
curses.set_tabsize(2)

# Push ch so the next getch() will return it.
ch = 'e'
curses.ungetch(ch)

# Update LINES and COLS. Useful for detecting manual screen resize.
curses.update_lines_cols()
# get terminal size with this:
print(curses.LINES,curses.COLS)




### Windows management


# Return a new window, whose left-upper corner is at (begin_y, begin_x), and whose height/width is nlines/ncols.
nlines, ncols, begin_y, begin_x = 30,30,3,3
window1 = curses.newwin(nlines, ncols, begin_y, begin_x)


# Paint character ch at (y, x) with attributes attr, overwriting any character previously painted at that location
y, x, n, ch, str = 3,3,3,'e','eee'
window1.addch(y, x, ch)


window1.addnstr(y, x, str, n)


curses.napms(1000)

# Terminating a curses application is much easier than starting one. You’ll need to call:
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
# to reverse the curses-friendly terminal settings. Then call the endwin() function to restore the terminal to its original operating mode.
curses.endwin()