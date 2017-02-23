from .edge import Edge
import logging
import copy
import datetime


class Graph(object):

    def __init__(self, problem):
        self.logger = logging.getLogger('graph_logger')

        self.problem = problem

        self.boundaries = list()
        self.obstacle_vertices = dict()
        self.get_boundaries()

        self.edges = list()
        self.vertices = list()
        self.create_edges()

    def create_edge_obstacles(self, count_max=2):
        """

        :param number_of_closest: Number of closest edges you will find for each one
        :return:
        """

        if self.problem.obstacles is None:
            return

        for obstacle in self.problem.obstacles:
            for boundary in obstacle.boundaries:
                self.edges.append(Edge(boundary[0], boundary[1], self, True))

        self.logger.info('Finished creating %i edges from boundaries' % len(self.edges))

        obstacles = copy.deepcopy(self.problem.obstacles)

        while len(obstacles) > 0:
            o_i = obstacles.pop(0)
            self.logger.info('Remaining Obstacles...%i' % len(obstacles))
            vertices_i = o_i.vertices

            for o_d in obstacles:
                vertices_d = o_d.vertices

                # Create a list of edges
                edges = list()
                for v_i in vertices_i:
                    for v_d in vertices_d:
                        edges.append(Edge(v_i, v_d, self))
                # Sort them out based on the weight
                self.add_edge_or_break(edges, count_max)

    def create_edge_robots(self, count_max=2):
        robots = copy.deepcopy(self.problem.robots)

        while len(robots) > 0:
            r_i = robots.pop(0)

            edges = list()
            for r_d in robots:
                edges.append(Edge(r_i.vertices, r_d.vertices, self, self.problem.obstacles is None))

            self.add_edge_or_break(edges, count_max)

    def create_robot_obstacle(self, count_max=2):
        robots = copy.deepcopy(self.problem.robots)
        obstacles = copy.deepcopy(self.problem.obstacles)

        for robot in robots:
            for obstacle in obstacles:

                edges = list()
                for vertex in obstacle.vertices:
                    edges.append(Edge(robot.vertices, vertex, self))

                self.add_edge_or_break(edges, count_max)

    def add_edge_or_break(self, edges, count_max):
        edges = sorted(edges, key=lambda e: e.weight)

        i = 0
        for edge in edges:
            if not edge.intersect_with_obstacles():
                self.edges.append(edge)
                i += 1
            if i >= count_max:
                break

    def create_edges(self):

        start_time = datetime.datetime.now()

        self.create_edge_obstacles()
        self.create_edge_robots()
        self.create_robot_obstacle(count_max=3)

        self.logger.info('There are %i vertices from robots, creating edges now' % len(self.vertices))

        self.logger.info('Finished creating %i edges' % len(self.edges))
        self.logger.info('The process took: %s' % str(datetime.datetime.now() - start_time))

    def get_boundaries(self):

        for obstacle in self.problem.obstacles:
            self.boundaries.extend(obstacle.boundaries)

            for vertex in obstacle.vertices:
                self.obstacle_vertices[vertex] = obstacle

        self.logger.info('Finished creating %i boundaries' % len(self.boundaries))

    def filter_boundaries(self, v_1, v_2, offset=None):

        boundaries = self.boundaries

        delta_y = v_2[1] - v_1[1]
        delta_x = v_2[0] - v_1[0]
        try:
            delta = delta_y / delta_x
        except ZeroDivisionError:
            delta = -1

        x_range = (v_1[0], v_2[0])

        y_range_min = min([delta * v_1[0], delta * v_2[0]])
        y_range_max = max([delta * v_1[0], delta * v_2[0]])
        y_range = (y_range_min, y_range_max)

        filtered_boundaries = list()
        for boundary in boundaries:

            if delta > 0:
                # First check X
                start_x = min(boundary[0][0], boundary[1][0])
                final_x = max(boundary[0][0], boundary[1][0])
                x_c_1 = start_x > min(x_range) and start_x < max(x_range)
                x_c_2 = final_x > min(x_range) and start_x < max(x_range)
                x_c = x_c_1 or x_c_2
                if not x_c:
                    continue

            # Check Y
            start_y = min(boundary[0][1], boundary[1][1])
            final_y = max(boundary[0][1], boundary[1][1])
            y_c_1 = start_y > min(y_range) and start_y < max(y_range)
            y_c_2 = final_y > min(y_range) and start_y < max(y_range)
            y_c = y_c_1 or y_c_2
            if not y_c:
                continue
            #
            # if min(boundary[0][1], boundary[1][0]) < min(y_range):
            #     continue
            # if max(boundary[0][1], boundary[1][1]) > max(x_range):
            #     continue

            filtered_boundaries.append(boundary)
        return filtered_boundaries
