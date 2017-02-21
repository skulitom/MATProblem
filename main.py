from utilities import custom_logger, parser, writer
from models import Solution
import visualization


def main_algorithm():
    custom_logger.start_logger()

    problems = parser.parse()

    # Example of Writing solution
    sol = Solution(question_number=1)

    l = list()
    c1 = [(-1.5, 1.5), (-1, 0)]
    c2 = [(-1, 0), (2, 2), (5, 0), (4.6, -3)]
    c3 = [(5, 0), (4.5, 3.5)]

    l.append(c1)
    l.append(c2)
    l.append(c3)

    sol.list_of_coordinates = l
    # writer.write_solution([sol])

    # Example Usage of visualization
    visualization.draw(problems[0], sol)

if __name__ == "__main__":
    main_algorithm()