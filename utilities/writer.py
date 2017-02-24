import logging
import os
from models import Solution


def write_solution(solutions):
    """

    :param solutions: list of solutions
    :return: output to a file with label solution_n.txt, where n is an incremental number
    """

    logger = logging.getLogger('main_logger')

    logger.info('Writing Solutions')
    n = 0
    file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    while os.path.isfile('%s/solutions/solution_%s.txt' % (file_path, str(n))):
        n += 1

    logger.info('Writing to solution_%s.txt' % str(n))
    with open('%s/solutions/solution_%s.txt' % (file_path, str(n)), 'w') as f:

        # Write team name and password
        # f.write('erumpent\n')  # team-name
        # f.write('j1kb4rrbduujb6fqvurrqdbvoc\n')  # password

        for sol in solutions:
            if type(sol) is not Solution:
                logger.critical('Argument should be list of solution, in models/solution.py')
                raise TypeError

            logger.info('Writing solution for %i' % sol.question_number)
            f.write('%i: ' % sol.question_number)

            solution_string = ''
            for coordinates in sol.list_of_coordinates:
                for coordinate in coordinates:
                    if type(coordinate) is not tuple:
                        logger.critical('Coordinate has to be type tuple')
                        raise TypeError

                    solution_string += '(%f, %f),' % (coordinate[0], coordinate[1])
                solution_string = solution_string[:-1] + ';'
            solution_string = solution_string[:-1] + '\n'

            f.write(solution_string)
            logger.info('Done writing solution for %i' % sol.question_number)

        f.close()
        logger.info('Writing solutions successful')