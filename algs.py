from typing import List
from routing_problem import RoutingProblem
from node import Node
from priority_queue import PriorityQueue
from utils import avg_time


def best_first_graph_search(problem: RoutingProblem, f) -> List[int]:
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


def find_ucs_route(source: int, target: int, f) -> List[int]:
    problem = RoutingProblem(source, target, cost=avg_time)
    return best_first_graph_search(problem, f=f)


def find_astar_route(source: int, target: int, g, h) -> List[int]:
    problem = RoutingProblem(source, target, cost=avg_time)
    return best_first_graph_search(problem, f=lambda x: g(x) + h(problem[x.state], problem[problem.goal]))


def find_idastar_route(source: int, target: int, g, h) -> List[int]:
    problem = RoutingProblem(source, target, cost=avg_time)
    start = Node(problem.s_start)
    f_limit = h(problem[start.state], problem[problem.goal])
    while True:
        sol, f_limit = dfs_countour(start, f_limit, problem, g, h=lambda x: h(problem[x.state], problem[problem.goal]))
        if sol is not None:
            return sol
        if f_limit is float('Inf'):
            return None


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
