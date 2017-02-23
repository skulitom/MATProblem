import math


class Obstacle(object):
    def __init__(self, vertices, problem):
        """

        :param vertices: list of vertices, in (x, y) format
        """
        self.vertices = vertices
        self.problem = problem

        # For easy access!
        self.x = vertices[0]
        self.y = vertices[1]

        self.boundaries = self.boundary_edges()

    def boundary_edges(self):

        edges = list()

        for i in range(0, len(self.vertices)):
            s = self.vertices[i]

            if i == len(self.vertices)-1:
                e = self.vertices[0]
            else:
                e = self.vertices[i+1]

            edges.append((s, e))

        return edges

    def find_neighbors(self, v):

        n = list()

        for edge in self.boundaries:
            if edge[0] == v:
                n.append(edge[1])
            elif edge[1] == v:
                n.append(edge[0])

        return n

    def find_path(self, v_1, v_2):
        s = list()
        dist, prev = self.dijkstra_path(v_1)

        u = v_2
        while prev[u] is not None:
            s.append(u)
            u = prev[u]
        s += [u]

        edges = list()
        for i in range(0, len(s)):
            a = s[i]

            if i == len(s) - 1:
                b = s[0]
            else:
                b = s[i + 1]

            edges.append((a, b))

        return edges[:-1]

    def dijkstra_path(self, v_1):
        # Using Dijkstra

        q = set()
        dist = dict()
        prev = dict()

        for v in self.vertices:
            dist[v] = float('inf')
            prev[v] = None
            q.add(v)

        dist[v_1] = 0

        while q:
            dist_q = {v: dist[v] for v in q}

            u = min(dist_q, key=lambda x: dist_q[x])
            q.remove(u)

            for v in self.find_neighbors(u):
                alt = dist[u] + self.calculate_weight(u, v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

        return dist, prev

    @staticmethod
    def calculate_weight(v1, v2):
        delta_x = v1[0] - v2[0]
        delta_y = v1[1] - v2[1]

        return math.sqrt(delta_x * delta_x + delta_y * delta_y)






