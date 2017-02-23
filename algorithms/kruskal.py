def kruskal_path(graph, edges):
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
