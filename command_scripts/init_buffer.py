
import pynput #keypress library
from pynput.keyboard import Key, Controller
import time


keyboard=Controller()

keyboard.press(Key.alt)

keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.release(Key.alt)

time.sleep(1)

keyboard.press('i')
keyboard.release('i')


time.sleep(1)

keyboard.press(Key.alt)

keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.release(Key.alt)
