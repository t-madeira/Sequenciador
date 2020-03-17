from pynput.mouse import Button, Controller
import time

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

def click_from_drag_to (Xfrom, Yfrom, Xto, Yto):
    mouse.position = (Xfrom, Yfrom)
    time.sleep(1)
    mouse.press(Button.left)
    time.sleep(1)
    mouse.position = (Xto, Yto)
    time.sleep(1)
    mouse.release(Button.left)

