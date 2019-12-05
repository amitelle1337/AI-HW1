class RoadsProblem:

    def __init__(self, roads, source, goal=None, cost=lambda x: 1):
        self.roads = roads
        self.s_start = source
        self.goal = goal
        self.cost = cost

    def actions(self, s):
        return self.roads[s].links

    def succ(self, s, a):
        return a.target

    def is_goal(self, s):
        return s == self.goal

    def step_cost(self, s, a):
        return self.cost(a)
