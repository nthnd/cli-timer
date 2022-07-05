#!/bin/python3
import traceback
import curses
from curses import wrapper
import time
seconds = 0
minutes = 0
hours = 0


def update(window):
    updateTime()
    updateScreen(window)


def updateTime():
    global seconds, minutes, hours
    seconds += 1
    if seconds >= 60:
        seconds = 0
        minutes += 1
    elif minutes >= 60:
        minutes = 0
        hours += 1


def updateScreen(window):
    global seconds
    window.clear()
    window.border()

    (maxY, maxX) = window.getmaxyx()

    window.addstr(maxY//2 - 2 ,maxX//2 - 3, ':    :')
    
    window.addstr(maxY//2 - 2 ,maxX//2 - 6,str(hours).zfill(2), curses.A_DIM)
    window.addstr(maxY//2 - 2 ,maxX//2 - 1,str(minutes).zfill(2),)
    window.addstr(maxY//2 - 2 ,maxX//2 + 4,str(seconds).zfill(2), curses.A_BOLD)

    window.addstr(maxY//2,maxX//2 - 11,'|' + 20*' ' + '|', curses.A_BOLD)
    window.addstr(maxY//2,maxX//2 - 10,(seconds//3 + 1)*' ', curses.A_REVERSE)
    
    window.addstr(maxY - 2,maxX//2 - 7,'q : quit, r: reset')

    window.refresh()


def resetTimer():
    global seconds, minutes, hours
    seconds, minutes, hours = 0, 0, 0


def main(window):
    global seconds, minutes, hours
    curses.curs_set(0)
    window.nodelay(True)
    ch = ''
    while True:
        update(window)
        curses.napms(1000)
        ch = window.getch()
        if ch == ord('r'):
            resetTimer()
        elif ch == ord('q'):
            break


wrapper(main)
