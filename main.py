from models import Graph
from utilities import custom_logger, parser, writer
import logging
import visualization
from multiprocessing import Process


def main_algorithm():
    problems = parser.parse()
    pb = problems[3]

    # Visualize is using process (non blocking)

    graph = Graph(pb, infinite_edge=False)
    # graph = Graph(pb, infinite_edge=True)

    # for edge in graph.edges:
    #     print("%s -> %s : %f" % (edge.start, edge.end, edge.weight))

    Process(target=visualization.draw(pb, edges=graph.edges)).start()

if __name__ == "__main__":
    custom_logger.start_logger()
    main_algorithm()



