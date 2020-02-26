from pynput.mouse import Button, Controller

mouse = Controller()

def right_click_at (x,y):
    mouse.position = (x, y)
    mouse.press(Button.right)
    mouse.release(Button.right)

def left_click_at (x,y):
    mouse.position = (x, y)
    mouse.press(Button.left)
    mouse.release(Button.left)

def double_left_click_at (x,y):
    mouse.position = (x, y)
    mouse.click(Button.left, 2)