
from PIL import ImageGrab


def take_screenshot():
    im = ImageGrab.grab()
    im.save('screenshot.png')
