import tkinter as tk
import pyautogui
import keyboard
from time import perf_counter

# variables
window = tk.Tk()
wx = 100
wy = 100
command_stopwatch_ctrl = 0

# constants
WINDOW_SIZE = 100

def showMenu () :
    global wx, wy
    wx, wy = pyautogui.position()
    window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+{int(wx)}+{int(wy)}")

def on_press_ctrl ():
    global command_stopwatch_ctrl
    command_stopwatch_ctrl = perf_counter()

def on_press_ctrlc ():
    global command_stopwatch_ctrl
    end = perf_counter()

    # the time difference between when the user presses Ctrl + C and when they press C.
    seconds = end - command_stopwatch_ctrl
    
    if (seconds < 0.5) :
        showMenu()

def prepareKeyboard():
    keyboard.add_hotkey('ctrl', on_press_ctrl)
    keyboard.add_hotkey('ctrl+c', on_press_ctrlc)

def resource_path(relative_path): # This function reads files as requested by the library (PyInstaller)
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return relative_path

def createWindow():
    global window, WINDOW_SIZE, wy, wx
    
    prepareKeyboard()

    window.configure(background="white")
    window.attributes('-topmost', True)
    window.attributes('-alpha', 0.5)
    window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+{wx}+{wy}")
    window.bind('<F3>', lambda e: window.destroy())
    window.overrideredirect(True) # without border

    window.mainloop()

createWindow()

