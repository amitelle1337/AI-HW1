import sys
from collections import deque
import random

from node import Node
from ways import load_map_from_csv


def bfs_span_tree(roads, start):
    open = deque([Node(start)])
    close = set()
    while open:
        next_node = open.popleft()
        close.add(next_node.state)
        for link in roads[next_node.state].links:
            s = link.target
            if s not in close and not find_state(s, open):
                new = Node(s, next_node)
                open.append(new)
    return close


def bfs_start_goal(roads, start, goal):
    open = deque([Node(start)])
    close = set()
    while open:
        next_node = open.popleft()
        if next_node.state is goal:
            return next_node.solution()
        close.add(next_node.state)
        for link in roads[next_node.state].links:
            s = link.target
            if s not in close and not find_state(s, open):
                new = Node(s, next_node)
                open.append(new)
    return None


def bfs_rand_goal(roads, start, rand_threshhold=10000, rand_count=1):
    open = deque([Node(start)])
    close = set()
    while open and (len(open) + len(close) <= rand_threshhold):
        next_node = open.popleft()
        close.add(next_node.state)
        for link in roads[next_node.state].links:
            s = link.target
            if s not in close and not find_state(s, open):
                new = Node(s, next_node)
                open.append(new)
    rand_goals = []
    seen = list(open) + list(close)
    random.seed(None)
    for i in range(rand_count):
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
    roads = load_map_from_csv()
    s = random.randint(0, len(roads))
    print(bfs_rand_goal(roads, s, rand_count=4))
