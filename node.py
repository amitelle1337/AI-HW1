class Node(object):
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def solution(self):
        curr = self
        path = []
        while curr is not None:
            path.append(curr.state)
            curr = curr.parent
        return path[::-1]
