from models import Graph
from utilities import custom_logger, parser, writer
import logging
import visualization
import copy
from algorithms import kruskal_path, dijkstra_path
from multiprocessing import Process


def main_algorithm():
    problems = parser.parse()

    logger = logging.getLogger('main_logger')

    pb = problems[8]

    graph = Graph(pb)
    graph.sort_edges()
    solution_edges = set()

    logger.info('Generating Kruskal MST')
    MST = kruskal_path(graph, graph.edges)
    logger.info('Generating Kruskal MST Complete')

    logger.info('Generating Dijkstra Routes')
    pb_robots = copy.deepcopy(pb.robots)
    while len(pb_robots) > 0:
        logger.info('Generating Dijkstra, remaining: %i' % len(pb_robots))
        r_i = pb_robots.pop(0)
        v_i = r_i.vertices

        for r in pb_robots:
            v_d = r.vertices
            solution_edges = solution_edges.union(set(dijkstra_path(v_i, v_d, graph.vertices, MST)))
    logger.info('Generating Dijkstra Routes Complete')
    logger.info('Visualizing the solution')
    # Visualize is using process (non blocking)
    Process(target=visualization.draw(pb, mst_edges=list(solution_edges), edges=graph.edges)).start()

if __name__ == "__main__":
    custom_logger.start_logger()
    main_algorithm()



