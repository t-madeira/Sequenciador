from pynput.mouse import Button, Controller

mouse = Controller()

def right_click_at (X,Y):
    mouse.position = (X,Y)
    mouse.press(Button.right)
    mouse.release(Button.right)

def left_click_at (X,Y):
    mouse.position = (X,Y)
    mouse.press(Button.left)
    mouse.release(Button.left)

def double_left_click_at (X,Y):
    mouse.position = (X,Y)
    mouse.click(Button.left, 2)