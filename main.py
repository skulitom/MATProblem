from models import Graph, Edge
from utilities import custom_logger, parser, writer
import logging
import visualization
import copy
from multiprocessing import Process


def main_algorithm():
    problems = parser.parse()
    pb = problems[0]

    graph = Graph(pb)
    graph.sort_edges()
    solution_edges = list()
    connected_edges = list()

    nodes = set()
    robots = set()
    pb_robots = set(pb.robots)

    for edge in graph.edges:
        # Find the shortest path between robots
        if edge.robots:
            if len(edge.robots) > 1:
                if robots == pb_robots:  # Found all robot-paths
                    break
                if not set(edge.robots).issubset(robots):
                    for robot in edge.robots:
                        robots.add(robot)
                    solution_edges.append(edge)
            else:
                # Start of the edge is a robot
                if edge.start in graph.robot_vertices and edge.end not in nodes:
                    nodes.add(edge.end)
                    solution_edges.append(edge)

                elif edge.end in graph.robot_vertices and edge.start in nodes:
                    nodes.add(edge.start)
                    solution_edges.append(edge)

        else:  # Edge from obstacle to obstacle or boundary
            if not edge.is_boundary:  # non-boundary edge
                nodes.add(edge.start)
                nodes.add(edge.end)
                solution_edges.append(edge)

    node_path_nodes = list(copy.deepcopy(nodes))
    while len(node_path_nodes) > 0:
        n_i = node_path_nodes.pop(0)
        for n_d in node_path_nodes:
            for obstacle in pb.obstacles:
                if n_i in obstacle.vertices and n_d in obstacle.vertices:
                    for edge in obstacle.find_path(n_i, n_d):
                        solution_edges.append(Edge(edge[0], edge[1], None))

    # Visualize is using process (non blocking)
    Process(target=visualization.draw(pb, mst_edges=solution_edges, edges=graph.edges)).start()

if __name__ == "__main__":
    custom_logger.start_logger()
    main_algorithm()



