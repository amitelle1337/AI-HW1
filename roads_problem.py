from ways import load_map_from_csv


class RoadsProblem:
    roads = None

    def __init__(self, source, goal=None, cost=lambda x: 1):
        self.s_start = source
        self.goal = goal
        self.cost = cost
        if RoadsProblem.roads is None:
            RoadsProblem.roads = load_map_from_csv()

    def actions(self, s):
        return RoadsProblem.roads[s].links

    def succ(self, s, a):
        return a.target

    def is_goal(self, s):
        return s == self.goal

    def step_cost(self, s, a):
        return self.cost(a)

    def __len__(self):
        return len(RoadsProblem.roads)
