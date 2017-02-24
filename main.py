from models import Graph, Edge, Solution
from utilities import custom_logger, parser, writer
from algorithms import kruskal_path, dijkstra_path, find_path
from multiprocessing import Process
import logging
import copy
import visualization


def main_algorithm(problem):
    logger = logging.getLogger('main_logger')

    logger.critical('Problem %i' % problem.question_number)
    # pb = problems[no]

    graph = Graph(problem)
    graph.sort_edges()
    solution_edges = set()

    logger.info('Generating Dijkstra Routes')
    pb_robots = copy.deepcopy(problem.robots)
    sol_robots = list()

    # Special for the first robot
    r_f = pb_robots.pop(0)
    r_f.awaken = True

    pb_robots = sorted(pb_robots, key=lambda robot: Edge(r_f.vertices, robot.vertices, None).weight)
    v = list()

    v.append(pb_robots[0].vertices)
    edges = dijkstra_path(v_1=r_f.vertices, v_2=pb_robots[0].vertices, vertices=graph.vertices, edges=graph.edges)
    r_f.track.extend(edges)
    sol_robots.append(r_f)

    solution_edges = solution_edges.union(set(edges))
    r_p = r_f  # Previous Robot
    pb_robots[0].awaken = True
    awake = 2
    while len(pb_robots) > 0:
        logger.debug('Generating Dijkstra, remaining: %i' % len(pb_robots))
        r_i = pb_robots.pop(0)

        prev, dist = find_path(v_1=r_i.vertices,
                               vertices=graph.vertices,
                               edges=graph.edges)

        pb_robots = sorted(pb_robots, key=lambda robot: dist[robot.vertices])

        robots = list()
        # Select Destination robots that have not been reached. They should not be a destination.
        for i in range(0, len(pb_robots)):
            if pb_robots[i].awaken:
                continue
            robots.append(pb_robots[i])

            if i < len(pb_robots)-1:
                robots.append(pb_robots[i+1])

            if len(robots) is 2:
                break

        for r in robots:
            edges = set(dijkstra_path(r_i.vertices, r.vertices, graph.vertices, graph.edges))  # Generated by Dijkstra

            found = False
            for edge in edges:

                for sol_edge in solution_edges:

                    if edge.start == sol_edge.start and edge.end == sol_edge.end:
                        found = True
                        break

                    if edge.start == sol_edge.end and edge.end == sol_edge.start:
                        found = True
                        break

            if found:
                r.awaken = False
                continue

            if r_i not in sol_robots:
                sol_robots.append(r_i)
                r_i.track.extend(edges)

            else:  # Second Path
                r_p.track.extend(edges)

            solution_edges = solution_edges.union(edges)
            r.awaken = True
            awake += 1

        r_p = r_i  # Previous Robot

    # logger.info('Generating Dijkstra Routes Complete')
    # logger.info('Visualizing the solution')

    # for robot in sol_robots:
    #     robot.sort_track()
    #     print("Robot: %s" % (robot.vertices,))
    #     for t in robot.track:
    #         print('%s -> %s' % (t.start, t.end))

    solution = Solution(question_number=problem.question_number, robots=sol_robots)
    logger.critical('Finished Writing Solution for %i')

    logger.info('%i Robots Awake' % awake)
    writer.write_solution([solution])
    print(solution.list_of_coordinates)
    # Visualize is using process (non blocking)
    # Process(target=visualization.draw(problem, mst_edges=list(solution_edges), edges=graph.edges)).start()

if __name__ == "__main__":
    custom_logger.start_logger()
    problems = parser.parse()
    # main_algorithm(problems[15])
    # Process(target=main_algorithm, args=(problems[1],)).start()
    for i in range(11, 20):
        Process(target=main_algorithm, args=(problems[i],)).start()
    # for problem in problems:

