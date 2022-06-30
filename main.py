#!/bin/python3
import curses
from curses import wrapper
import time

seconds = 0
minutes = 0
hours = 0


def formatTime():
    return f"Seconds : {seconds}\nMinutes : {minutes}\nHours : {hours}"


def updateTime():
    global seconds, minutes, hours
    seconds += 1
    if seconds >= 60 :
        minutes += 1
        seconds = 0
    if minutes >= 60 :
        hours += 1
        minutes = 0


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    while True:
        try: 
            key = stdscr.getkey()
        except: 
            key = None
        if key == 'q':
            break
        
        timePassed = formatTime()
        
        stdscr.clear()
        stdscr.addstr("Press q to quit\n\n")
        stdscr.addstr(timePassed)
        stdscr.refresh()
        
        time.sleep(1)
        updateTime()


wrapper(main)
