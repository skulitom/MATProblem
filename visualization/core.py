import matplotlib.pyplot as plt
import matplotlib.patches as patches
import logging
from matplotlib.path import Path


def draw_polygon(verts, color='green', width=2, fill=True):
    """

    :param verts: List of vertices
    :param color: Color of polygon line (default is green)
    :param width: Width of polygon (default is 2)
    :param fill: Fill (default is True)
    :return: patch (Polygon), supply list of this to the draw.
    """

    logger = logging.getLogger('visual_logger')
    if len(verts) < 3:
        logger.critical('2 vertices are not polygons.')
        raise ValueError

    codes = list()
    codes.append(Path.MOVETO)

    for i in range(2, len(verts)):
        codes.append(Path.LINETO)

    codes.append(Path.CLOSEPOLY)
    print(codes)
    path = Path(verts, codes)

    patch = patches.PathPatch(path, facecolor=color, linewidth=width, fill=fill)

    return patch


def draw(polygons, x_axis=None, y_axis=None):
    """

    :param polygons: list of Polygon that is returned from draw_polygon
    :param x_axis: how long is y-axis
    :param y_axis: how long is y-axis
    :return: UI with polygons!
    """

    logger = logging.getLogger('visual_logger')
    if type(polygons) is not list:
        logger.critical('Please supply a list of polygons.')
        raise TypeError

    fig = plt.figure()
    ax = fig.add_subplot(111)  # Start with white background

    for polygon in polygons:
        ax.add_patch(polygon)

    ax.margins(x=.01, y=.01)

    if x_axis is not None:
        ax.set_xlim(-x_axis, x_axis)

    if y_axis is not None:
        ax.set_ylim(-y_axis, y_axis)

    plt.show()
