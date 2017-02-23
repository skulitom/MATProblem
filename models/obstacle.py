import math


class Obstacle(object):
    def __init__(self, vertices, problem):
        """

        :param vertices: list of vertices, in (x, y) format
        """
        self.vertices = vertices
        self.problem = problem

        # For easy access!
        self.x = vertices[0]
        self.y = vertices[1]

        self.boundaries = self.boundary_edges()

    def boundary_edges(self):

        edges = list()

        for i in range(0, len(self.vertices)):
            s = self.vertices[i]

            if i == len(self.vertices)-1:
                e = self.vertices[0]
            else:
                e = self.vertices[i+1]

            edges.append((s, e))

        return edges








