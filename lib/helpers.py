import math
import tkinter as tk
from typing import Union

PI = 3.141592
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (235, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 235)


def mark(canvas: tk.Canvas, coord: Union[list, tuple], co):
    size = 8
    x = coord[0]
    y = coord[1]
    d = round(math.sqrt(2) / 2 * size) - 1
    canvas.create_oval(x - size, y - size, x + size, y + size, fill="", outline=co)
    canvas.create_line(x - d, y - d, x + d + 1, y + d + 1, fill=co)
    canvas.create_line(x - d, y + d, x + d + 1, y - d - 1, fill=co)


def outtext(canvas: tk.Canvas, text: str, coords: Union[list, tuple], co):
    textId = canvas.create_text(
        coords[0], coords[1], text=text, font=("Consolas", 14), fill=co, anchor="nw"
    )
    return canvas.bbox(textId)


def pset(canvas: tk.Canvas, coords: Union[list, tuple], co):
    canvas.create_line(coords[0], coords[1], coords[0] + 1, coords[1], fill=co)
