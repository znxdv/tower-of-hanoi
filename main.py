import keyboard
import style
import tutorial
import time

def exits():
    style.clearScreen()
    style.ctext(style.BOLD + style.WHITE + style.ITALIC + "Thank You ^^" + style.RESET, -6, 0)
    print(10 * '\n')
    exit

def about():
    style.clearScreen()
    style.ctext(style.BOLD + style.LIGHTWHITE + style.ITALIC + 'This Tower of Hanoi project is intended as an Assesment of Learning for "Algorithm Design and Analysis" subject.', -56, -5)
    style.ctext('Our Team :', -5, -2)
    style.ctext('Mhd. Fauzan Devinto - 2602225201', -16, 1)
    style.ctext('Muhammad Raihan Zuhair Aryamehr - 2602198440', -22, 2)
    style.ctext('Naufal Fairuza - 2602192090', -13, 3)
    style.ctext('Timothy Abimanju Paudy Rumoku - 2602198882' + style.RESET, -23, 4)
    style.ctext(style.DIM + 'Press Space to continue.', -12, 7)
    while True:
        if keyboard.read_event(suppress = True).name == "space":
            break
    main()
    
def main():
    style.clearScreen()
    style.hidePrompt(hides=True)

    style.ctext(style.BOLD + style.LIGHTWHITE + "===> Tower Of Hanoi <===" + style.RESET, -12, -3)
    txt1, txt2, txt3, txt4 = True, False, False, False
    indices = [txt1, txt2, txt3, txt4]
    relationships = {0: [0], 1: [1], 2: [2], 3: [3]}

    while True:
        style.ctext((style.LIGHTWHITE +   " [Play] "   + style.RESET) if txt1 else (style.DIM +   " [Play] "   + style.RESET), -13, 3)
        style.ctext((style.LIGHTWHITE + " [Tutorial] " + style.RESET) if txt2 else (style.DIM + " [Tutorial] " + style.RESET), 6, 3)
        style.ctext((style.LIGHTWHITE +   " [About] "  + style.RESET) if txt3 else (style.DIM +   " [About] "  + style.RESET), -14, 6)
        style.ctext((style.LIGHTWHITE +   " [Exit] "   + style.RESET) if txt4 else (style.DIM +   " [Exit] "   + style.RESET), 6, 6)

        key = keyboard.read_event(suppress=True)

        if key.name == "left" or key.name == "right":
            indices = [txt1, txt2, txt3, txt4]
            relationships = {0: [1], 1: [0], 2: [3], 3: [2]}
        elif key.name == "up" or key.name == "down":
            relationships = {0: [2], 1: [3], 2: [0], 3: [1]}
            indices = [txt1, txt2, txt3, txt4]
        
        newIndices = indices.copy()
        for idx, related_indices in relationships.items():
            if indices[idx]:
                newIndices[idx] = False
                for relatedIdx in related_indices:
                    newIndices[relatedIdx] = True
        txt1, txt2, txt3, txt4 = newIndices
        time.sleep(0.2)
        if key.name == "enter":
            break
        else:
            continue

    if txt1:
        main()
    if txt2:
        tutorial.tutorial()
    if txt3:
        about()
    if txt4:
        exits()

if __name__ == "__main__":
    main()