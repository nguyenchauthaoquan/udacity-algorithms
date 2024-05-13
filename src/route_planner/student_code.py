import math
from queue import PriorityQueue


def shortest_path(graph, start, goal):
    shortest_paths = PriorityQueue()

    shortest_paths.put(start, 0)

    traversed_paths = {start: None}
    g = {start: 0}

    while not shortest_paths.empty():
        current_node = shortest_paths.get()

        if current_node == goal:
            get_paths(traversed_paths, start, goal)

        for node in graph.roads[current_node]:
            h = calculate_h(graph.intersections[current_node], graph.intersections[node])
            f = g[current_node] + h

            if node not in g or f < g[node]:
                g[node] = f
                h = calculate_h(graph.intersections[current_node], graph.intersections[node])
                f = f + h
                shortest_paths.put(node, f)
                traversed_paths[node] = current_node
    return get_paths(traversed_paths, start, goal)


def calculate_h(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


def get_paths(traversed_paths, start, goal):
    current_node = goal
    paths = [current_node]

    while current_node != start:
        current_node = traversed_paths[current_node]
        paths.append(current_node)
    paths.reverse()

    return paths
