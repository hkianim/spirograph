import tkinter as tk
from lib import shapes
from lib.spirogram import Spirogram
from tests import test1

window = tk.Tk()
window.title("Spirograph - By H. Kiani Moghaddam (c) 2024")
window.resizable(False, False)


def drawSpirogram():
    radius1 = int(spinRadius1.get())
    radius2 = int(spinRadius2.get())
    radius3 = int(spinRadius3.get())
    cycles = int(spinCycles.get())
    co = "#7092BE"
    spirogram = Spirogram(radius1, radius2, radius3)

    x = int(canvas["width"]) // 2
    y = int(canvas["height"]) // 2
    axis = shapes.Axis(canvas, (x, y))

    spirogram.draw(axis, co, cycles)


def widgetChanged():
    drawSpirogram()


def buttonDrawClickHandler():
    drawSpirogram()


panelLeft = tk.Frame(master=window, bg="aliceblue")
# radius1:
labelRadius1 = tk.Label(master=panelLeft, text="Radius 1", fg="grey", bg="aliceblue")
labelRadius1.pack(fill=tk.X, padx=10)
defRadius1 = tk.StringVar(window)
defRadius1.set(267)
spinRadius1 = tk.Spinbox(
    master=panelLeft, from_=1, to=1000, textvariable=defRadius1, command=widgetChanged
)
spinRadius1.pack(fill=tk.X, padx=10)
# radius2:
labelRadius2 = tk.Label(master=panelLeft, text="Radius 2", fg="grey", bg="aliceblue")
labelRadius2.pack(fill=tk.X, padx=10)
defRadius2 = tk.StringVar(window)
defRadius2.set(152)
spinRadius2 = tk.Spinbox(
    master=panelLeft, from_=1, to=1000, textvariable=defRadius2, command=widgetChanged
)
spinRadius2.pack(fill=tk.X, padx=10)
# radius3:
labelRadius3 = tk.Label(master=panelLeft, text="Radius 3", fg="grey", bg="aliceblue")
labelRadius3.pack(fill=tk.X, padx=10)
defRadius3 = tk.StringVar(window)
defRadius3.set(87)
spinRadius3 = tk.Spinbox(
    master=panelLeft, from_=1, to=1000, textvariable=defRadius3, command=widgetChanged
)
spinRadius3.pack(fill=tk.X, padx=10)
# cycles:
labelCycles = tk.Label(master=panelLeft, text="Cycles", fg="grey", bg="aliceblue")
labelCycles.pack(fill=tk.X, padx=10)
defCycles = tk.StringVar(window)
defCycles.set(28)
spinCycles = tk.Spinbox(
    master=panelLeft, from_=1, to=1000, textvariable=defCycles, command=widgetChanged
)
spinCycles.pack(fill=tk.X, padx=10)

buttonDraw = tk.Button(master=panelLeft, text="Draw", command=buttonDrawClickHandler)

buttonDraw.pack(fill=tk.X, padx=10, pady=5)
panelLeft.pack(side=tk.LEFT, fill=tk.Y)

panelRight = tk.Frame(master=window)
canvas = tk.Canvas(panelRight, width=500, height=500, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
panelRight.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# test1.testAll(canvas)


window.mainloop()
