from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class Obstacle(object):
    def __init__(self, vertices):
        """

        :param vertices: list of vertices, in (x, y) format
        """
        self.vertices = vertices

        # For easy access!
        self.x = vertices[0]
        self.y = vertices[1]


    def in_area(self, point):
        """

        :param point: point of interest
        :return: Boolean to tell if it's in the shape
        """
        return Polygon(self.vertices).contains(Point(point))








