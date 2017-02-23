from math import sqrt
import copy


class Robot(object):
    def __init__(self, vertex, problem):
        self.vertices = vertex
        self.problem = problem  # Parent object

        # For easy access!
        self.x = vertex[0]
        self.y = vertex[1]

        # Solution
        self.track = list()

        self.awaken = False

    def closest_robot(self):
        robots = self.problem.robots

        if len(robots) is 0:
            return None

        closest_robot = None
        second_closest_robot = None
        distance = float('inf')
        for rb in robots:
            # print("Vertices of robot: %s" % (rb.vertices,))
            x_dis = abs(rb.x - self.x)
            y_dis = abs(rb.y - self.y)
            dis = sqrt(x_dis * x_dis + y_dis * y_dis)

            if dis < distance:
                distance = dis
                second_closest_robot = closest_robot
                closest_robot = rb

        return closest_robot, second_closest_robot

    def second_closest_robot(self, closest_robot):
        robots = self.problem.robots

        return self.closest_robot()

    def two_nearest(self):
        closest_robot = self.closest_robot()
        return closest_robot, self.second_closest_robot(closest_robot)

    def sort_track(self):

        track = copy.deepcopy(self.track)
        # print('Vertices: %s ' % (self.vertices,))
        # [print('Track: %s -> %s' % (t.start, t.end, )) for t in self.track]
        track_shallow = list()

        for t in track:
            # Find Beginning Edge
            if t.start == self.vertices:
                self.track[0] = t
                track.remove(t)
                break

            if t.end == self.vertices:
                t.reverse()
                self.track[0] = t
                track.remove(t)
                break

        i = 1
        while len(track) > 0:
            found = False
            for t in track:
                if t.start == self.track[i-1].end:
                    self.track[i] = t
                    track.remove(t)
                    i += 1
                    found = True
                    break

                if t.end == self.track[i-1].end:
                    t.reverse()
                    self.track[i] = t
                    track.remove(t)
                    i += 1
                    found = True
                    break

            if not found:
                print('[************] Failed to sort the track')
                raise ValueError
