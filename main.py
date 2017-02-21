from utilities import custom_logger, parser, writer
from models import Solution
import visualization


def main_algorithm():
    custom_logger.start_logger()

    # problems = parser.parse()

    # Example of Writing solution
    writeSolution(Solution(question_number=1))
    writeSolution(Solution(question_number=2))
    # Example Usage of visualization
    problems = parser.parse()
    drawSolution(problems[12])

def writeSolution(sol):
    l = list()
    for i in range(0, 10):
        l.append((float(i), float(i+10)))

    sol.list_of_coordinates = [l]
    writer.write_solution([sol])


def drawSolution(problem):
    polygons = list()

    for obstacle in problem.obstacles:
        polygons.append(visualization.draw_polygon(obstacle.vertices, width=0.1))
        point = (0.5, 0.5)
        print(obstacle.in_area(point=point))

    visualization.draw(polygons)


if __name__ == "__main__":
    main_algorithm()