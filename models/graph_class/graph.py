from .edge import Edge
import logging
import copy
import datetime


class Graph(object):

    def __init__(self, problem, self_edge=False, infinite_edge=False):
        self.logger = logging.getLogger('graph_logger')

        self.problem = problem

        self.boundaries = list()
        self.obstacle_vertices = dict()
        self.get_boundaries()

        self.edges = list()
        self.vertices = list()
        self.create_edges()

    def create_edge_obstacles(self, sorted_way=True, number_of_closest=2):
        """

        :param sorted_way: You can either use sort_way or normal min each loop. Sorted is recommend for
                            larger obstacles.
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
                # sorted(edges, key=lambda edge: edge.weight)
                if sorted_way:
                    edges = sorted(edges, key=lambda edge: edge.weight)

                    i = 0
                    for edge in edges:
                        if not edge.intersect_with_obstacles():
                            self.edges.append(edge)
                            i += 1
                        if i > 2:
                            break
                    continue

                # Or try the one with minimum
                n = 0
                while n < number_of_closest and len(edges) > 0:
                    min_edge = min(edges, key=lambda edge: edge.weight)
                    edges.remove(min_edge)

                    # Check if it works
                    while min_edge.intersect_with_obstacles():
                        if len(edges) == 0:
                            min_edge = None
                            break

                        min_edge = min(edges, key=lambda edge: edge.weight)

                        edges.remove(min_edge)

                    # If it works, add it
                    if min_edge:
                        self.edges.append(min_edge)

    def create_edges(self):

        start_time = datetime.datetime.now()

        self.create_edge_obstacles()

        for robot in self.problem.robots:
            # Robot's vertices are the coordinates that represent the position of the robot
            self.vertices.append(robot.vertices)

        self.logger.info('There are %i vertices from robots, creating edges now' % len(self.vertices))

        # Create edge from robots to robots / robots to obstacles
        vertices = self.vertices
        while len(vertices) > 0:
            v_i = vertices.pop(0)

            # Create R - R
            for v_r in vertices:
                edge = Edge(v_i, v_r, self, self.problem.obstacles is None)
                if edge.intersect_with_obstacles():
                    continue
                else:
                    self.edges.append(edge)

            # Create R - O
            for v_o in self.obstacle_vertices:
                edge = Edge(v_i, v_o, self)
                if edge.intersect_with_obstacles():
                    continue
                else:
                    print('%s -> %s' % (edge.start, edge.end,))
                    self.edges.append(edge)

        self.logger.info('Finished creating %i edges' % len(self.edges))
        self.logger.info('The process took: %s' % str(datetime.datetime.now() - start_time))

    def get_boundaries(self):

        for obstacle in self.problem.obstacles:
            self.boundaries.extend(obstacle.boundaries)

            for vertex in obstacle.vertices:
                self.obstacle_vertices[vertex] = obstacle

        self.logger.info('Finished creating %i boundaries' % len(self.boundaries))

