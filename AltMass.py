import keyboard
import pyautogui
import time


print("Inicitating TSAMASS")
with open('id.txt') as f:

    lines = [line.rstrip() for line in f]

    my_list_len = len(lines)
with open('date.txt') as r:

    dateLines = [line.rstrip() for line in r]

    my_lists_len = len(dateLines)

for i in range(0, my_list_len):
        
    if len(lines[i]) == 9:
               
        pyautogui.click(1700,270)

        keyboard.write(lines[i])
        time.sleep(.5)
        pyautogui.press('enter')
        keyboard.write(dateLines[i])
        pyautogui.press('enter')
                
        pyautogui.click(1700,210)

        print('correct ID#', i, lines[i])

        time.sleep(1)
