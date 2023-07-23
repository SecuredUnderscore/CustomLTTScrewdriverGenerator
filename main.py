# Pillow library: pip install Pillow
from enum import Enum
from PIL import Image


class Colors(Enum):
    BLACK = "1"
    PINK = "2"
    DARKBLUE = "3"
    LIGHTBLUE = "4"
    GREEN = "5"
    YELLOW = "6"
    ORANGE = "7"
    RED = "8"


def start(directioncolor, ringcolor, handlecolor, bitselectorcolor):
    baseimage = Image.open("base.png")
    directionchanger = Image.open(f"./directionchangers/{directioncolor.value}.png")
    ring = Image.open(f"./rings/{ringcolor.value}.png")
    handle = Image.open(f"./handles/{handlecolor.value}.png")
    bitselector = Image.open(f"./bitselectors/{bitselectorcolor.value}.png")
    newscrewdriver = Image.alpha_composite(baseimage, directionchanger)
    newscrewdriver = Image.alpha_composite(newscrewdriver, ring)
    newscrewdriver = Image.alpha_composite(newscrewdriver, handle)
    newscrewdriver = Image.alpha_composite(newscrewdriver, bitselector)
    newscrewdriver.save("GENERATEDSCREWDRIVER.png")


if __name__ == '__main__':
    # Set parameters here
    start(directioncolor=Colors.LIGHTBLUE, ringcolor=Colors.PINK, handlecolor=Colors.LIGHTBLUE, bitselectorcolor=Colors.BLACK)
