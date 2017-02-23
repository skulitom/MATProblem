from models import Graph, Edge
from utilities import custom_logger, parser, writer
import logging
import visualization
import copy
from algorithms import kruskal_path, dijkstra_path
from multiprocessing import Process


def main_algorithm():
    problems = parser.parse()

    logger = logging.getLogger('main_logger')

    pb = problems[28]

    graph = Graph(pb)
    graph.sort_edges()
    solution_edges = set()

    logger.info('Generating Kruskal MST')
    MST = kruskal_path(graph, graph.edges, initial_robot=pb.robots[0])
    logger.info('Generating Kruskal MST Complete, size: %i' % len(MST))
    # Process(target=visualization.draw(pb, mst_edges=MST, edges=graph.edges)).start()

    logger.info('Generating Dijkstra Routes')
    pb_robots = copy.deepcopy(pb.robots)

    # Special for the first robot
    r_f = pb_robots.pop(0)

    pb_robots = sorted(pb_robots, key=lambda robot: Edge(r_f.vertices, robot.vertices, None).weight)
    [print(robot.vertices) for robot in pb_robots]
    v = list()
    if len(pb_robots) > 0:
        v.append(pb_robots[0].vertices)

    for a in v:
        solution_edges = solution_edges.union(set(dijkstra_path(r_f.vertices, a, graph.vertices, MST)))

    while len(pb_robots) > 0:
        logger.info('Generating Dijkstra, remaining: %i' % len(pb_robots))
        r_i = pb_robots.pop(0)
        v_i = r_i.vertices

        pb_robots = sorted(pb_robots, key=lambda robot: Edge(v_i, robot.vertices, None).weight)

        v = list()
        if len(pb_robots) > 0:
            v.append(pb_robots[0].vertices)
        if len(pb_robots) > 1:
            v.append(pb_robots[1].vertices)

        for a in v:
            solution_edges = solution_edges.union(set(dijkstra_path(v_i, a, graph.vertices, MST)))

        # for idx, r in enumerate(pb_robots):
        #     v_d = r.vertices
        #     logger.info('%i out of %i' % (idx, len(pb_robots)))
        #     solution_edges = solution_edges.union(set(dijkstra_path(v_i, v_d, graph.vertices, MST)))
    logger.info('Generating Dijkstra Routes Complete')
    logger.info('Visualizing the solution')
    # Visualize is using process (non blocking)
    Process(target=visualization.draw(pb, mst_edges=list(solution_edges), edges=graph.edges)).start()

if __name__ == "__main__":
    custom_logger.start_logger()
    main_algorithm()
