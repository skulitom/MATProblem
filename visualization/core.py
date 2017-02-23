import matplotlib.pyplot as plt
import matplotlib.patches as patches
import logging
import numpy
from matplotlib.path import Path


logger = logging.getLogger('visual_logger')


def draw_polygon(vertices, color=None, width=2, fill=True):
    """

    :param vertices: List of vertices
    :param color: Color of polygon line (default is green)
    :param width: Width of polygon (default is 2)
    :param fill: Fill (default is True)
    :return: patch (Polygon), supply list of this to the draw.
    """

    if len(vertices) < 3:
        logger.critical('2 vertices or less are not polygons.')
        raise ValueError

    vertices.append(vertices[-1])

    codes = list()
    codes.append(Path.MOVETO)

    for i in range(2, len(vertices)):
        codes.append(Path.LINETO)

    codes.append(Path.CLOSEPOLY)

    path = Path(vertices, codes)

    if color is None:
        patch = patches.PathPatch(path, facecolor=numpy.random.rand(3, 1), linewidth=width, fill=fill)
    else:
        patch = patches.PathPatch(path, facecolor=color, linewidth=width, fill=fill)

    return patch


def draw(problem, edges=None, solution=None, x_axis=None, y_axis=None):
    """

    :param problem: problem to be drawn
    :param edges: edges of the graph
    :param solution: solution to the problem (optional)
    :param x_axis: how long is y-axis (optional)
    :param y_axis: how long is y-axis (optional)
    :return: UI with polygons!
    """

    fig = plt.figure()
    fig.suptitle(('Problem %s' % str(problem.question_number)), fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)  # Start with white background

    if problem.obstacles is not None:

        polygons = list()
        for obstacle in problem.obstacles:
            polygons.append(draw_polygon(obstacle.vertices))

        if type(polygons) is not list:
            logger.critical('Please supply a list of polygons.')
            raise TypeError

        for polygon in polygons:
            ax.add_patch(polygon)

    for robot in problem.robots:
        plt.plot(robot.x, robot.y, 'o')

    if edges is not None:
        for edge in edges:
            x_coordinates = [edge.start[0], edge.end[0]]
            y_coordinates = [edge.start[1], edge.end[1]]

            # plt.plot(x_coordinates, y_coordinates, color=numpy.random.rand(3, 1))
            plt.plot(x_coordinates, y_coordinates, color='grey')

    if solution is not None:
        line_coordinates = solution.list_of_coordinates
        for line_coordinate in line_coordinates:
            x_coordinates = list()
            y_coordinates = list()

            for coordinate in line_coordinate:
                x_coordinates.append(coordinate[0])
                y_coordinates.append(coordinate[1])

            plt.plot(x_coordinates, y_coordinates, color=numpy.random.rand(3, 1))

    if x_axis is not None:
        ax.set_xlim(-x_axis, x_axis)

    if y_axis is not None:
        ax.set_ylim(-y_axis, y_axis)

    ax.margins(x=.1, y=.1)

    plt.show()
