from ways import load_map_from_csv


class RoutingProblem:
    roads = load_map_from_csv()

    def __init__(self, source, goal=None, cost=lambda x: 1):
        self.s_start = source
        self.goal = goal
        self.cost = cost

    @staticmethod
    def actions(s):
        return RoutingProblem.roads[s].links

    @staticmethod
    def succ(s, a):
        if s == a.source:
            return a.target
        raise Exception('Not Valid Operation')

    def is_goal(self, s):
        return s == self.goal

    def step_cost(self, s, a):
        if s == a.source:
            return self.cost(a)
        raise Exception('Not Valid Operation')

    def __len__(self):
        return len(RoutingProblem.roads)

    def __getitem__(self, item):
        return RoutingProblem.roads[item]
