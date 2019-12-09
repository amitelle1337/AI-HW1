from collections import deque
import random
from routing_problem import RoutingProblem
from node import Node


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


def breadth_first_graph_search(problem):
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
        rand_goals.append(seen[pos])
        seen.remove(seen[pos])
    return rand_goals


def find_state(state, node_list):
    for node in node_list:
        if node.state is state:
            return True
    return False


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    num_problems = 100
    rand_count = 2
    prob = RoutingProblem(None)
    with open('problems.csv', 'w+') as f:
        for i in range(num_problems // rand_count):
            s = random.randint(0, len(prob))
            prob = RoutingProblem(s)
            for t in bfs_rand_goal(prob, rand_count=rand_count):
                f.write(str(s) + ',' + str(t) + '\n')
