
## PyAutoGUI 
PyAutoGUI module lets your Python scripts control the mouse and keyboard to automate interactions with other applications. 
The API is designed to be as simple. 
PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.
pip install pyautogui
## How is it useful?
This technique is known as graphical user interface automation, or GUI automation for short.
With GUI automation, your programs can do anything that a human user sitting at the computer can do, except spill coffee on the keyboard.
This technique is particularly useful for tasks that involve a lot of mindless clicking or filling out of forms.
Features
## Moving and clicking the mouse.
#Get the XY position of the mouse.
>>> currentMouseX, currentMouseY = pyautogui.position() 

#Move the mouse to XY coordinates.
>>> pyautogui.moveTo(100, 150) 

#Click the mouse.
>>> pyautogui.click()          

#Move the mouse to XY coordinates and click it.
>>> pyautogui.click(100, 200)  

#Find where button.png appears on the screen and click it.
>>> pyautogui.click('button.png') 

#Move the mouse to XY coordinates and double click it.
>>> pyautogui.doubleClick()    


## Typing and pressing keys
#type with quarter-second pause in between each key
>>> pyautogui.write('Hello world!', interval=0.25)  

#Press the Esc key. All key names are in pyautogui.KEY_NAMES
>>> pyautogui.press('esc')     

#Press the Shift key down and hold it.
>>> pyautogui.keyDown('shift') 

#Press the left arrow key 4 times.
>>> pyautogui.press(['left', 'left', 'left', 'left']) 

#Let go of the Shift key.
>>> pyautogui.keyUp('shift')   

#Make an alert box appear and pause the program until OK is clicked.
>>> pyautogui.alert('This is the message to be displayed.') 

# Press the Ctrl-C hotkey combination.
>>> pyautogui.hotkey('ctrl', 'c') 

## Screenshot functions:
#returns a Pillow/PIL Image object
>>> pyautogui.screenshot()  

#returns a Pillow/PIL Image object, and saves it to a file
>>> pyautogui.screenshot('screenshot.png')  

#If you have an image file of something you want to click on, you can find it on the screen with locateOnScreen().

#returns (left, top, width, height) of first place it is found
>>> pyautogui.locateOnScreen('looksLikeThis.png')  

#returns the XY coordinates of the middle of where the image is found on the screen
>>> pyautogui.locateCenterOnScreen('looksLikeThis.png')  
