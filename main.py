#!/bin/python3
import curses
from curses import wrapper
import time

seconds = 0
minutes = 0
hours = 0



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
        
        
        stdscr.clear()
        stdscr.border()
        (maxY, maxX) = stdscr.getmaxyx()

        stdscr.addstr(maxY//2 - 2, maxX//2 - 1 , str(seconds).zfill(2), curses.A_BOLD)
        stdscr.addstr(maxY//2, maxX//2-11, '[                      ]')
        stdscr.addstr(maxY//2, maxX//2-10, seconds//3*' ', curses.A_REVERSE)
        minutesMessage = 'Minutes : ' + str(minutes).zfill(2)
        hoursMessage = 'Hours : ' + str(hours).zfill(2)
        stdscr.addstr(maxY//2 + 2, maxX//2 - len(minutesMessage)//2, minutesMessage)
        stdscr.addstr(maxY//2 + 3, maxX//2 - len(hoursMessage)//2, hoursMessage)
        stdscr.addstr(maxY-2, maxX//2 - 7, "Press q to quit")

        stdscr.refresh()
        time.sleep(1)
        updateTime()


wrapper(main)
