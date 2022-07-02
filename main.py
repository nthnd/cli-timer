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
    global seconds, minutes, hours
    curses.curs_set(0)
    stdscr.nodelay(True)

    while True:
        try: 
            key = stdscr.getkey()
        except: 
            key = None
        if key == 'q':
            break
        elif key == 'r':
            seconds = 0
            minutes = 0
            hours = 0
        
        
        stdscr.clear()
        stdscr.border()
        (maxY, maxX) = stdscr.getmaxyx()
        winWidth = 24
        winHeight = 10
        win = curses.newwin(winHeight, winWidth, maxY//2 - winHeight//2, maxX//2 - winWidth//2)


        win.addstr(winHeight//2 - 2, winWidth//2 - 1 , str(seconds).zfill(2), curses.A_BOLD)
        win.addstr(winHeight//2, winWidth//2-11, '[                    ]')
        win.addstr(winHeight//2, winWidth//2-10, (seconds//3 + 1)*' ', curses.A_REVERSE)
        minutesMessage = 'Minutes : ' + str(minutes).zfill(2)
        hoursMessage = 'Hours : ' + str(hours).zfill(2)
        win.addstr(winHeight//2 + 2, winWidth//2 - len(minutesMessage)//2, minutesMessage)
        win.addstr(winHeight//2 + 3, winWidth//2 - len(hoursMessage)//2, hoursMessage)
        footerMessage = "\'q\' : quit\t\'r\' : restart"
        stdscr.addstr(maxY-2, maxX//2 - len(footerMessage)//2, footerMessage)
        win.refresh()
        time.sleep(1)
        updateTime()


wrapper(main)
