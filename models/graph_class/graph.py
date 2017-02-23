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

        self.vertices = set()
        self.robot_vertices = list()
        self.edges = list()
        self.create_edges()

    def create_edge_obstacles(self, count_max=1):
        """

        :param count_max: number of edges between obstacles
        :return:
        """

        self.logger.info('Creating edges between obstacles')

        if self.problem.obstacles is None:
            return

        for obstacle in self.problem.obstacles:

            for boundary in obstacle.boundaries:
                edge = Edge(boundary[0], boundary[1], self, True)
                edge.obstacle = obstacle
                self.vertices.add(boundary[0])
                self.vertices.add(boundary[1])
                self.edges.append(edge)

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
                    self.vertices.add(v_i)
                    for v_d in vertices_d:
                        self.vertices.add(v_d)
                        edges.append(Edge(v_i, v_d, self))
                # Sort them out based on the weight
                self.add_edge_or_break(edges, count_max)

        self.logger.info('Creating edges between obstacles COMPLETE')

    def create_edge_robots(self, count_max=2):

        self.logger.info('Creating edges between robots')

        robots = copy.deepcopy(self.problem.robots)
        while len(robots) > 0:
            r_i = robots.pop(0)
            self.vertices.add(r_i.vertices)
            self.robot_vertices.append(r_i.vertices)
            edges = list()
            for r_d in robots:
                self.vertices.add(r_d.vertices)
                self.robot_vertices.append(r_d.vertices)
                edges.append(Edge(r_i.vertices, r_d.vertices, self, self.problem.obstacles is None,
                                  robots=[r_i, r_d]))

            self.add_edge_or_break(edges, count_max)

        self.logger.info('Creating edges between robots COMPLETE')

    def create_robot_obstacle(self, count_max=1):

        self.logger.info('Creating edges between robots and obstacles')

        robots = copy.deepcopy(self.problem.robots)
        obstacles = copy.deepcopy(self.problem.obstacles)

        if obstacles is None:
            return

        for idx, robot in enumerate(robots):
            self.logger.info('%i out of %i robots' % (idx, len(robots)))
            for obstacle in obstacles:
                edges = list()
                for vertex in obstacle.vertices:
                    edges.append(Edge(robot.vertices, vertex, self,robots=[robot]))

                self.add_edge_or_break(edges, count_max)

        self.logger.info('Creating edges between robots and obstacles COMPLETE')

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
        self.create_robot_obstacle()
        self.logger.info('The process took: %s' % str(datetime.datetime.now() - start_time))

    def get_boundaries(self):
        if self.problem.obstacles is not None:
            for obstacle in self.problem.obstacles:
                self.boundaries.extend(obstacle.boundaries)

                for vertex in obstacle.vertices:
                    self.obstacle_vertices[vertex] = obstacle

            self.logger.info('Finished creating %i boundaries' % len(self.boundaries))

    def sort_edges(self):
        self.edges = sorted(self.edges, key=lambda edge: edge.weight)
