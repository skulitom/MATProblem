from models import Edge


def dijkstra_path(v_1, v_2, vertices, edges, dist=None, prev=None):
    s = list()

    if not (dist and prev):
        dist, prev = find_path(v_1, vertices, edges)

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


def find_path(v_1, vertices, edges):
    # Using Dijkstra

    q = set()
    dist = dict()
    prev = dict()

    for v in vertices:
        dist[v] = float('1000')
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


def find_neighbors(v, edges):

    n = list()

    for edge in edges:
        if edge.start == v:
            n.append(edge.end)
        elif edge.end == v:
            n.append(edge.start)

    return n


def find_edge(v1, v2, edges):
    for edge in edges:
        if edge.start == v1 and edge.end == v2:
            return edge
        if edge.start == v2 and edge.end == v1:
            return edge

    edge = Edge(v1, v2, None)
    return edge