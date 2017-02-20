class Problem(object):
    def __init__(self, question_number):
        self.question_number = question_number

        # Array of Obstacle
        self.obstacles = None

        # Array of Robot
        self.robots = None


class Robot(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class Obstacle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y