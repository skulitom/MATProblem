def kruskal_path(graph, edges, initial_robot):
    sets = list()

    sets.append({initial_robot.vertices})
    for v in graph.vertices:
        if v is not initial_robot.vertices:
            sets.append({v})

    sol_edges = list()
    print(sets)
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
