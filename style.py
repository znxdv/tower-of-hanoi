import os
import shutil

RESET      = "\x1b[0m"
BOLD       = "\x1b[1m"
DIM        = "\x1b[2m"
ITALIC     = "\x1b[3m"

RED        = "\x1b[31m"
LIGHTWHITE = "\x1b[97m"

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def hidePrompt(hides):
    if hides:
        print("\033[?25l", end='', flush = True)
    else:
        print("\033[?25h", end='', flush = True)

def ctext(text, x=0, y=0):
    column, lines = shutil.get_terminal_size()
    centerX = column // 2
    centerY = (lines - 1) // 2
    finalX = centerX + x
    finalY = centerY + y
    gotoxy(finalX, finalY)
    print(text)

def gotoxy(x, y):
    print("\033[%d;%dH" % (y, x), end='')