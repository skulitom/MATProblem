from utilities import custom_logger, parser
import visualization


def main_algorithm():
    custom_logger.start_logger()

    problems = parser.parse()

    # Example Usage of visualization

    problem = problems[1]

    polygons = list()

    for obstacle in problem.obstacles:
        polygons.append(visualization.draw_polygon(obstacle.vertices, width=0.1))
        point = (0.5, 0.5)
        print(obstacle.in_area(point=point))

    visualization.draw(polygons)


if __name__ == "__main__":
    main_algorithm()
