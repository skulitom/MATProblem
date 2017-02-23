from models import Graph
from utilities import custom_logger, parser, writer
import logging
import visualization
from multiprocessing import Process


def main_algorithm():
    problems = parser.parse()
    pb = problems[5]

    graph = Graph(pb)

    # Access to Graph
    # for edge in graph.edges:
    #
    # Visualize is using process (non blocking)
    Process(target=visualization.draw(pb, edges=graph.edges)).start()

if __name__ == "__main__":
    custom_logger.start_logger()
    main_algorithm()



