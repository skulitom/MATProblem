import sys
import logging
import re
from models import *


def parse():

    logger = logging.getLogger('main_logger')
    logger.info('Starting Parsing')

    try:
        # List of problems to store parsed Problems
        problems = list()

        with open('robots.mat') as input_text:
            for line in input_text:

                # Remove whitespaces
                line = line.replace(' ','').replace('\n', '')

                try:
                    question_number = int(line[:line.index(':')])
                    problem = Problem(question_number=question_number)

                    logger.info('Parsing question : %i' % problem.question_number)

                except ValueError as e:
                    logger.critical('ValueError %s' % (str(e)))
                    sys.exit(1)

                # Remove the question number part
                line = line[line.index(':')+1:]

                try:
                    i = line.index('#')

                except ValueError:
                    i = -1

                if i:
                    # If it has obstacles, parse the robots and obstacles
                    robots = line[:i].split('),')

                    # Obstacles (still in string)
                    obstacles = line[i + 1:].split(';')
                    problem_obstacles = list()

                    # Parse the tuples
                    for obstacle in obstacles:
                        coordinates = obstacle.split('),')

                        # Parse the string list
                        coordinates[:] = [coordinate.strip('()') for coordinate in coordinates]
                        coordinates[:] = [coordinate.split(',') for coordinate in coordinates]

                        for coordinate in coordinates:
                            try:
                                obs = Obstacle(
                                    x=float(coordinate[0]),
                                    y=float(coordinate[1])
                                )
                                problem_obstacles.append(obs)

                            except ValueError as e:
                                logger.critical('ValueError %s' % str(e))
                                sys.exit(1)

                        problem.obstacles = problem_obstacles

                else:  # There is no obstacle
                    robots = line.split('),')

                robots[:] = [robot.strip('()') for robot in robots]
                robots[:] = [robot.split(',') for robot in robots]
                try:
                    problem_robots = list()

                    for robot in robots:
                        rb = Robot(
                            x=float(robot[0]),
                            y=float(robot[1])
                        )
                        problem_robots.append(rb)

                    problem.robots = problem_robots

                except ValueError as e:
                    logger.critical('ValueError %s' % str(e))
                    sys.exit(1)

                logger.info('Successfully parsed Question number : %i' % problem.question_number)
                problems.append(problem)

        return problems

    except IOError as e:
        logger.critical('IOError %i: %s' % (e.errno, e.strerror))
        sys.exit(1)

