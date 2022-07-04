#!/bin/python3
import traceback
import curses
from curses import wrapper

seconds = 0
minutes = 0
hours = 0

def update(stdscr):
    updateTime()
    updateScreen(stdscr)

def updateTime():
    global seconds, minutes, hours
    seconds += 1
    if seconds >= 60:
        seconds = 0
        minutes += 1
    elif minutes >= 60:
        minutes = 0
        hours += 1

def updateScreen(stdscr):
    global seconds
    stdscr.clear()
    stdscr.addstr((seconds//3 + 1)*' ', curses.A_REVERSE)
    stdscr.refresh()

def main(stdscr):
    global seconds, minutes, hours
    curses.curs_set(0)
    stdscr.nodelay(True)
    try: 
        ch = ''
        while ch != ord('q'):
            update(stdscr)
            stdscr.timeout(1000)
            ch = stdscr.getch()
    except: 
        traceback.print_exc()
wrapper(main)
