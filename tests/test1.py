import tkinter as tk
from lib import helpers, shapes


def testAll(canvas: tk.Canvas):
    # testMark(canvas)
    # testOutText(canvas)
    testAxis(canvas)
    # testPoint(canvas)
    # testLine(canvas)
    testCircle(canvas)


def testMark(canvas: tk.Canvas):
    helpers.mark(canvas, (10, 10), "red")


def testOutText(canvas: tk.Canvas):
    bbox = helpers.outtext(canvas, "Spirogram", (10, 10), "blue")
    helpers.mark(canvas, (bbox[0], bbox[1]), "red")
    helpers.mark(canvas, (bbox[2], bbox[3]), "red")


def testAxis(canvas: tk.Canvas):
    x = int(canvas["width"]) // 2
    y = int(canvas["height"]) // 2
    axis = shapes.Axis(canvas, (x, y))
    axis.draw(200, "grey")


def testPoint(canvas: tk.Canvas):
    x = int(canvas["width"]) // 2
    y = int(canvas["height"]) // 2
    axis = shapes.Axis(canvas, (x, y))
    point = shapes.Point((50, 50))
    point.mark(axis, "red")


def testLine(canvas: tk.Canvas):
    x = int(canvas["width"]) // 2
    y = int(canvas["height"]) // 2
    axis = shapes.Axis(canvas, (x, y))
    line = shapes.Line(shapes.Point((10, 10)), shapes.Point((250, 50)))
    line.draw(axis, "green")
    line.getStart().mark(axis, "orange")
    line.getEnd().mark(axis, "orange")


def testCircle(canvas: tk.Canvas):
    x = int(canvas["width"]) // 2
    y = int(canvas["height"]) // 2
    axis = shapes.Axis(canvas, (x, y))
    circle = shapes.Circle(shapes.Point((20, 30)), 30)
    circle.draw(axis, "purple", True)
