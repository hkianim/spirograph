from lib import helpers, shapes


class Spirogram:

    def __init__(self, radius1: float, radius2: float, radius3: float):
        self._radius1: float = radius1
        self._radius2: float = radius2
        self._radius3: float = radius3

    def draw(self, axis: shapes.Axis, co: int, cycles: int = 1):

        axis.getCanvas().delete("all")
        center1 = shapes.Point((0, 0))
        center2 = shapes.Point((self._radius1 - self._radius2, 0))
        point = shapes.Point((self._radius1 - self._radius2 + self._radius3, 0))
        point.draw(axis, co)

        lastPoint = point
        for a1 in range(1, 360 * cycles):
            arc = a1 / 360 * (2 * helpers.PI * self._radius1)
            a2 = arc / (2 * helpers.PI * self._radius3) * 360
            newPoint = point.rotate(center1.asCartesian(), a1).rotate(
                center2.rotate(center1.asCartesian(), a1).asCartesian(), -a2
            )
            line = shapes.Line(lastPoint, newPoint)
            line.draw(axis, co)
            lastPoint = newPoint
