#!/bin/python3
import curses
from curses import wrapper
import time
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    minutes = 0
    seconds = 0
    hours = 0
    while True:
        try: 
            key = stdscr.getkey()
        except: 
            key = None
        if key == 'q':
            break
        
        timePassed = f"Seconds : {seconds}\nMinutes : {minutes}\n Hours : {hours}"  
        stdscr.clear()
        stdscr.addstr(timePassed)
        stdscr.refresh()
        time.sleep(1)
        seconds+=1
wrapper(main)
