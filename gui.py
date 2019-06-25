# Author : SUSHANT KUMAR
# USAGE : Just to copy code from a tutorial video and speed up your work.
# Feel free to modify the code and don't forget the credits Haha...
from tkinter import *
from pytesseract import image_to_string
from PIL import Image
from screenshot import take_screenshot


# Global Canvas

tk = Tk()
can = Canvas(tk, width=300, height=100, bg='white')
can.pack()

can.create_text(100, 50, text="1. Press crtl+x for taking screen shot\n2. Select the text you want to copy. \n3. Press crtl+c to Copy!\n4. Enjoy \n Made with Love by Sushant Kumar")
# Opeining Screen for display


# Creating another window for working canvas for the screenshot

working_root = Toplevel(tk)
working_canvas = Canvas(working_root, width=1920, height=1080, bg='black')
working_canvas.pack()
img = PhotoImage(file="screenshot.png")
working_canvas.create_image(0, 0, image=img, anchor=NW)
working_root.destroy()

# Global variables to work with ScreenShots
startX = 0
startY = 0
endX = 0
endY = 0
buttonFlag = 0


def drawRectangle():
    working_canvas.delete("all")
    working_canvas.create_image(0, 0, image=img, anchor=NW)
    working_canvas.create_rectangle(startX, startY, endX, endY,
                                    fill='#fff', stipple="gray12")


def callback3(event):
    print("Mouse is moving")
    print("Moving at", event.x, event.y)
    global buttonFlag, startX, startY, endX, endY
    if buttonFlag == 0:
        startX = event.x
        startY = event.y
        buttonFlag = 1
    endX = event.x
    endY = event.y
    drawRectangle()


def callback1(event):
    global buttonFlag, startX, startY, endX, endY
    working_canvas.delete("all")
    working_canvas.create_image(0, 0, image=img, anchor=NW)
    startX = event.x
    startY = event.y


def callback2(event):
    global buttonFlag, startX, startY, endX, endY
    print("released at", event.x, event.y)
    endX = event.x
    endY = event.y
    print("released at", startX, startY, endX, endY)
    buttonFlag = 0
    drawRectangle()


def copy_to_clipboard(event):
    # Trying to read the content from the image
    try:
        im = Image.open("screenshot.png")
        cropped = im.crop((startX, startY, endX, endY))
        cropped.save('cropped.png')
        print('Done')
    except:
        print("Something went wrong!")

    text = image_to_string('cropped.png', lang='eng')
    working_root.clipboard_clear()
    working_root.clipboard_append(text)
    working_root.update()  # now it stays on the clipboard after the window is closed


def take_screenshot_process(event):
    global img
    take_screenshot()

    global working_root, working_canvas, img

    working_root = Toplevel(tk)
    working_canvas = Canvas(working_root, width=1920, height=1080, bg='black')
    working_canvas.pack()
    img = PhotoImage(file="screenshot.png")
    working_canvas.create_image(0, 0, image=img, anchor=NW)
    working_canvas.bind("<Button-1>", callback1)
    working_canvas.bind("<ButtonRelease-1>", callback2)
    working_canvas.bind("<B1-Motion>", callback3)
    working_canvas.bind("<Control-c>", copy_to_clipboard)
    working_canvas.focus_set()
    working_canvas.pack()


can.bind("<Control-x>", take_screenshot_process)
can.focus_set()
can.pack()

tk.mainloop()
