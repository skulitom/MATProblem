from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class Obstacle(object):
    def __init__(self, vertices):
        """

        :param vertices: list of vertices, in (x, y) format
        """
        self.vertices = vertices

    def in_area(self, point):

        return Polygon(self.vertices).contains(Point(point))








