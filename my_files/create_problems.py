import csv
from collections import deque
import random

from my_files.routing_problem import RoutingProblem
from my_files.node import Node
from my_files.utils import est_time


def bfs_span_tree(problem):
    frontier = deque([Node(problem.s_start)])  # FIFO queue
    closed_list = set()
    while frontier:
        node = frontier.popleft()
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
    return closed_list


def bfs_graph(problem):
    frontier = deque([Node(problem.s_start)])  # FIFO queue
    closed_list = set()
    while frontier:
        node = frontier.popleft()
        if problem.is_goal(node.state):
            return node.solution()
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
    return None


def bfs_rand_goal(problem, rand_threshhold=200, rand_count=1):
    frontier = deque([Node(problem.s_start)])  # FIFO queue
    closed_list = set()
    while frontier and len(frontier) + len(closed_list) < rand_threshhold:
        node = frontier.popleft()
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
    rand_goals = []
    seen = [node.state for node in frontier] + list(closed_list)
    random.seed(None)
    for _ in range(rand_count):
        pos = random.randint(0, len(seen) - 1)
        rand_goals.append(seen.pop(pos))
    return rand_goals


def find_state(state, node_list):
    for node in node_list:
        if node.state is state:
            return True
    return False


def main():
    from sys import argv

    assert len(argv) == 1
    num_problems = 100
    rand_count = 2
    problem = RoutingProblem(None)
    probs = []

    for i in range(num_problems // rand_count):
        s = random.randint(0, len(problem))
        problem = RoutingProblem(s)
        for t in bfs_rand_goal(problem, rand_count=rand_count):
            probs.append((s, t))

    probs.sort(key=lambda p: est_time(problem[p[0]], problem[p[1]]))

    with open('../problems.csv', 'w+', newline='') as problem_file:
        problem_writer = csv.writer(problem_file)
        for p in probs:
            problem_writer.writerow(p)


if __name__ == '__main__':
    main()
