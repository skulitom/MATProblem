from utilities import custom_logger, parser, writer
from models import Solution
import visualization


def main_algorithm():
    custom_logger.start_logger()

    # problems = parser.parse()

    # Example of Writing solution
    sol = Solution(question_number=1)

    l = list()
    for i in range(0, 10):
        l.append((float(i), float(i+10)))

    sol.list_of_coordinates = [l]
    writer.write_solution([sol])
    # Example Usage of visualization


if __name__ == "__main__":
    main_algorithm()