# Opening zoom and join a meeting at a specified time
import pyautogui
import time
import datetime

meeting_id = " 123 4567 8912"
while True:
    current_time = datetime.datetime.now()

    if current_time.hour == 9: # Checks if the time is 9 am
        # Locates the Zoom icon on screen then double clicks it
        pyautogui.doubleClick(pyautogui.locateCenterOnScreen('Zoom-Icon.JPG',
                                                             confidence=0.9))
        time.sleep(1)
        # Locates the "Join meeting" icon on screen then clicks it
        pyautogui.click(pyautogui.locateCenterOnScreen('Join-Meeting.JPG',
                                                       confidence=0.9))
        pyautogui.write(meeting_id, interval=0.25)
        pyautogui.press('enter')
        exit()
