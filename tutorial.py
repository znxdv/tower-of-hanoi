import main
import style
import keyboard

def stepbystep(disks, source, aux, target, yOff, move):
    if disks == 1:
        move[0] += 1
        style.ctext(f"{move} Move disk 1 from {source} to {target}", -14, yOff)
        return yOff + 1
    yOff = stepbystep(disks-1, source, target, aux, yOff, move)
    move[0] += 1
    style.ctext(f"{move} Move disk {disks} from {source} to {target}", -14, yOff)
    yOff += 1
    yOff = stepbystep(disks-1, aux, source, target, yOff, move)
    return yOff
    
def tutorial():
    style.hidePrompt(hides = False)
    style.clearScreen()
    style.ctext("This menu calculates the most optimal steps for Tower of Hanoi with fewer than 100 disks and provides step-by-step solutions for up to 5 disks.", -71, -3)
    style.ctext("Enter the number of disks you want to calculate : ", -25, 0)
    style.gotoxy(106, 15)
    disks = int(input(''))
    while True:
        if disks < 1:
            style.ctext(style.RED + "Please enter a positive number of disks." + style.RESET, -20, 3)
        elif disks > 99:
            style.ctext(style.RED + "Please enter a number of disks that is less than 100." + style.RESET, -26, 3)
        else:
            break

        style.ctext(style.DIM + "Press Space to continue." + style.RESET, -13, 5)
        style.hidePrompt(hides=True)
        if keyboard.read_event(suppress = True).name == "space":
            tutorial()
    
    steps = 2**disks - 1
    formatSteps = '{:,}'.format(steps)
    if disks < 6:
        style.clearScreen()
        style.ctext(style.BOLD + f"The most optimal steps for {disks} disks is {formatSteps}" + style.RESET, -len(formatSteps)/2 - 19, -(steps/2 + 3))
        move = [0]
        stepbystep(disks, 'A', 'B', 'C', -(steps/2 + 0.5), move)
        style.ctext(style.DIM + 'Press ESC to go back to the main menu or Press Space to re-calculate.' + style.RESET, -32, steps/2 + 1.5)
    else:
        style.ctext(style.LIGHTWHITE + f"The most optimal steps for {disks} disks is {formatSteps}" + style.RESET, -len(formatSteps)/2 - 19, 3)
        style.ctext(style.DIM + 'Press ESC to go back to the main menu or Press Space to re-calculate.' + style.RESET, -32, 6)
    style.hidePrompt(hides = True)
    while True:
        key_event = keyboard.read_event(suppress = True)
        if key_event.name == "space":
            tutorial()
        elif key_event.name == "esc":
            main.main()