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
            # Calculate f(n) = g(n) + h(n); with h(n) is the weight between 2 vertices, g is the weight vertex
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
    """
    Calculate the h value between start and goal.
    :param start: The start node
    :param goal: The end node
    :return: h value between start and goal
    """
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


def get_paths(traversed_paths, start, goal):
    """
    Gets the paths from start to goal from traversed paths
    :param traversed_paths: The traversed paths from graph
    :param start: The start node
    :param goal: The goal node
    :return: All paths from start to goal from traversed paths
    """
    current_node = goal
    paths = [current_node]

    while current_node != start:
        current_node = traversed_paths[current_node]
        paths.append(current_node)
    paths.reverse()

    return paths
