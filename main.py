from models import Graph, Edge
from utilities import custom_logger, parser, writer
import logging
import visualization
import math
import copy
from multiprocessing import Process


def main_algorithm():
    problems = parser.parse()
    pb = problems[3]

    graph = Graph(pb)
    graph.sort_edges()
    solution_edges = list()

    MST = kruskal(graph, graph.edges)

    pb_robots = copy.deepcopy(pb.robots)
    while len(pb_robots) > 0:
        r_i = pb_robots.pop(0)
        v_i = r_i.vertices

        for r in pb_robots:
            v_d = r.vertices
            solution_edges.extend(find_path(v_i, v_d, graph.vertices, MST))
            print(solution_edges)
    # Visualize is using process (non blocking)
    Process(target=visualization.draw(pb, mst_edges=solution_edges, edges=graph.edges)).start()


def kruskal(graph, edges):
    sets = list()
    for v in graph.vertices:
        sets.append({v})

    sol_edges = list()

    edges = sorted(edges, key=lambda edge: edge.weight)
    for edge in edges:
        if find_set(sets, edge.start) != find_set(sets, edge.end):
            sol_edges.append(edge)

            s1 = find_set(sets, edge.start)
            s2 = find_set(sets, edge.end)

            sets.remove(s1)
            sets.remove(s2)

            sets.append(s1.union(s2))

    return sol_edges


def find_set(sets, v1):
    for s in sets:
        if v1 in s:
            return s


def find_neighbors(v, edges):

    n = list()

    for edge in edges:
        if edge.start == v:
            n.append(edge.end)
        elif edge.end == v:
            n.append(edge.start)

    return n


def find_path(v_1, v_2, vertices, edges):
    s = list()
    dist, prev = dijkstra_path(v_1, vertices, edges)

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

        edges.append(find_edge(a, b, edges))

    return edges[:-1]


def dijkstra_path(v_1, vertices, edges):
    # Using Dijkstra

    q = set()
    dist = dict()
    prev = dict()

    for v in vertices:
        dist[v] = float('inf')
        prev[v] = None
        q.add(v)

    dist[v_1] = 0

    while q:
        dist_q = {v: dist[v] for v in q}

        u = min(dist_q, key=lambda x: dist_q[x])
        q.remove(u)

        for v in find_neighbors(u, edges):
            edge = find_edge(u, v, edges)
            alt = dist[u] + edge.weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def find_edge(v1, v2, edges):
    for edge in edges:
        if edge.start == v1 and edge.end == v2:
            return edge
        elif edge.start == v2 and edge.end == v1:
            return edge

    return Edge(v1, v2, None)


def calculate_weight(v1, v2):
    delta_x = v1[0] - v2[0]
    delta_y = v1[1] - v2[1]

    return math.sqrt(delta_x * delta_x + delta_y * delta_y)

if __name__ == "__main__":
    custom_logger.start_logger()
    main_algorithm()



