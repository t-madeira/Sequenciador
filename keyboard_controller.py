from pynput.keyboard import Key, Controller

keyboard = Controller()

def type_this(str):
    keyboard.type(str)

def press_this(key):
    keyboard.press(key)
    keyboard.release(key)

def press_this_with_ALT (str):
    with keyboard.pressed(Key.alt):
        keyboard.press(str)
        keyboard.release(str)

def press_this_with_LSHIFT (key):
    with keyboard.pressed(Key.shift_l):
        keyboard.press(key)
        keyboard.release(key)




