class Solution(object):
    def __init__(self, question_number, robots):
        self.question_number = question_number

        self.solution_edges = list()

        # Nested loops of coordinates (for robot path)
        self.robots = robots
        self.list_of_coordinates = None

        self.parse_robot_track()

    def parse_robot_track(self):
        coordinates = list()
        for robot in self.robots:
            tracks = list()
            tracks.append(robot.vertices)
            for track in robot.track:
                tracks.append(track.end)

            coordinates.append(tracks)

        self.list_of_coordinates = coordinates

