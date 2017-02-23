from math import sqrt
from utilities import intersect, modified_intersect


class Edge(object):
    def __init__(self, node_s, node_e, graph, is_boundary=False, robots=None):
        """

        :param node_s: starting_node
        :param node_e: end_node
        """

        self.graph = graph

        self.start = node_s
        self.end = node_e

        self.robots = robots

        self.is_boundary = is_boundary
        self.obstacle = None

        x_dis = abs(self.start[0] - self.end[0])
        y_dis = abs(self.start[1] - self.end[1])

        self.weight = sqrt(x_dis * x_dis + y_dis * y_dis)

    def intersect_with_obstacles(self):

        if self.is_boundary:
            return False

        boundaries = self.graph.boundaries
        # boundaries = self.graph.filter_boundaries(self.start, self.end)
        vertices = self.graph.obstacle_vertices

        if (self.start, self.end) not in boundaries:

            # Check if its between the boundaries or the robots and the boundaries
            # 1. Boundaries
            if self.start in vertices and self.end in vertices:
                if vertices[self.start] == vertices[self.end]:
                    return True
                else:
                    for boundary in self.graph.boundaries:
                        if modified_intersect(self.start, self.end, boundary[0], boundary[1]):
                            return True
                    return False

            # 2. Boundary & Robot
            for boundary in boundaries:
                if boundary[0] == self.start or boundary[1] == self.start:
                    continue

                if boundary[0] == self.end or boundary[1] == self.end:
                    continue

                if intersect(self.start, self.end, boundary[0], boundary[1]):
                    return True

            return False
