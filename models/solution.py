class Solution(object):
    def __init__(self, question_number):
        self.question_number = question_number

        self.solution_edges = list()

        # Nested loops of coordinates (for robot path)
        self.list_of_coordinates = None

    # def parse_solution_edges(self):
    #     for edge in self.solution_edges:
