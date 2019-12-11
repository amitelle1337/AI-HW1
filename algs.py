from typing import List
from routing_problem import RoutingProblem
from node import Node
from priority_queue import PriorityQueue
from utils import avg_time, path_cost, est_time


def best_first_graph_search(problem: RoutingProblem, f) -> (List[int], float):
    node = Node(problem.s_start)
    frontier = PriorityQueue(f)  # Priority Queue
    frontier.append(node)
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node.solution(), node.path_cost
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None, None


def find_ucs_route(problem: RoutingProblem) -> (List[int], float):
    return best_first_graph_search(problem, f=path_cost)


def find_astar_route(problem: RoutingProblem) -> (List[int], float):
    return best_first_graph_search(problem, f=lambda node: path_cost(node) + est_time(problem[node.state],
                                                                                      problem[problem.goal]))


def find_idastar_route(problem: RoutingProblem) -> (List[int], float):
    start = Node(problem.s_start)
    f_limit = est_time(problem[start.state], problem[problem.goal])
    while True:
        sol, f_limit = dfs_countour(start, f_limit, problem, path_cost,
                                    h=lambda node: est_time(problem[node.state], problem[problem.goal]))
        if sol is not None:
            return sol, f_limit
        if f_limit is float('Inf'):
            return None, None


def dfs_countour(node: Node, f_limit: float, problem: RoutingProblem, g, h) -> (List[int], float):
    f = g(node) + h(node)
    if f > f_limit:
        return None, f
    if problem.goal is node.state:
        return node.solution(), f_limit
    next_f = float('Inf')
    for s in node.expand(problem):
        sol, new_f = dfs_countour(s, f_limit, problem, g, h)
        if sol is not None:
            return sol, f_limit
        next_f = min(next_f, new_f)
    return None, next_f
