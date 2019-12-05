from roads_problem import RoadsProblem
from node import Node
from priority_queue import PriorityQueue
from utils import avg_time
from ways import load_map_from_csv


def best_first_graph_search(problem, f):
    node = Node(problem.s_start)
    frontier = PriorityQueue(f)  # Priority Queue
    frontier.append(node)
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node.solution()
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None


def find_ucs_route(source, target, f):
    return best_first_graph_search(RoadsProblem(load_map_from_csv(), source, target, cost=avg_time), f=f)


def find_astar_route(source, target, f, h):
    return best_first_graph_search(RoadsProblem(load_map_from_csv(), source, target, cost=avg_time),
                                   f=lambda x: f(x) + h(X))
