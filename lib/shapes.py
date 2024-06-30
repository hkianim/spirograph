import tkinter as tk
import math
from typing import Union
from lib import helpers

CARTESIAN = 1
POLAR = 2


class Axis:
    def __init__(self, canvas: tk.Canvas, center: Union[list, tuple]):
        self._canvas = canvas
        self._center = tuple(center)

    def getCanvas(self) -> tk.Canvas:
        return self._canvas

    def getCenter(self) -> tuple:
        return self._center

    def draw(self, size: int, co):
        self._canvas.create_line(
            self._center[0] - size,
            self._center[1],
            self._center[0] + size,
            self._center[1],
            fill=co,
        )
        self._canvas.create_line(
            self._center[0],
            self._center[1] - size,
            self._center[0],
            self._center[1] + size,
            fill=co,
        )


class Point:
    def __init__(self, coords: Union[list, tuple], type: int = CARTESIAN):
        self._type: int = type
        self._coords: tuple = coords

    def asCartesian(self) -> tuple:
        if self._type == CARTESIAN:
            return self._coords
        else:
            r = self._coords[0]
            t = math.radians(self._coords[1])
            x = r * math.cos(t)
            y = r * math.sin(t)
            return (x, y)

    def asPolar(self) -> tuple:
        if type == POLAR:
            return self._coords
        else:
            x = self._coords[0]
            y = self._coords[1]
            r = math.sqrt(x * x + y * y)
            if r == 0:
                a = 0
            else:
                a = math.asin(y / r)
            return (r, a)

    def toScreen(self, center: Union[list, tuple]) -> tuple:
        x = round(center[0] + self.asCartesian()[0])
        y = round(center[1] - self.asCartesian()[1])
        return (x, y)

    def move(self, relCoords: Union[list, tuple]):
        x = self.asCartesian()[0] + relCoords[0]
        y = self.asCartesian()[1] + relCoords[1]
        return Point((x, y))

    # center: Cartesian coords
    # alpha: Angle in degrees
    def rotate(self, center: Union[list, tuple], alpha: float):
        x = self.asCartesian()[0] - center[0]
        y = self.asCartesian()[1] - center[1]
        relPoint1 = Point((x, y))
        r = relPoint1.asPolar()[0]
        a = relPoint1.asPolar()[1] + alpha
        relPoint2 = Point((r, a), POLAR)
        x = relPoint2.asCartesian()[0] + center[0]
        y = relPoint2.asCartesian()[1] + center[1]
        return Point((x, y))

    def draw(self, axis: Axis, co) -> "Point":
        helpers.pset(axis.getCanvas(), self.toScreen(axis.getCenter()), co)
        return self

    def mark(self, axis: Axis, co: int) -> "Point":
        helpers.mark(axis.getCanvas(), self.toScreen(axis.getCenter()), co)
        return self


class Line:
    def __init__(self, start: Point, end: Point):
        self._start: Point = start
        self._end: Point = end

    def getStart(self):
        return self._start

    def getEnd(self):
        return self._end

    def draw(self, axis: Axis, co: int):
        start = self._start.toScreen(axis.getCenter())
        end = self._end.toScreen(axis.getCenter())
        axis.getCanvas().create_line(start[0], start[1], end[0], end[1], fill=co)


class Circle:
    def __init__(self, center: Point, radius: float):
        self._center: Point = center
        self._radius: float = radius

    def rotate(self, center: Union[list, tuple], alpha: float) -> "Circle":
        newCenter = self._center.rotate(center, alpha)
        return Circle(newCenter, self._radius)

    def draw(self, axis: Axis, co: int, drawCenter: bool = False) -> "Circle":
        topleft = self._center.move((-self._radius, -self._radius)).toScreen(
            axis.getCenter()
        )
        bottomright = self._center.move((self._radius, self._radius)).toScreen(
            axis.getCenter()
        )
        axis.getCanvas().create_oval(
            topleft[0], topleft[1], bottomright[0], bottomright[1], fill="", outline=co
        )

        if drawCenter:
            self.drawCenter(axis, co)

        return self

    def drawCenter(self, axis: Axis, co: int) -> "Circle":
        helpers.pset(axis.getCanvas(), self._center.toScreen(axis.getCenter()), co)
        return self
