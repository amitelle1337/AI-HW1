import csv

import algs
from routing_problem import RoutingProblem
from ways import draw
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('problems.csv', 'r', newline='') as problem_file:
        problem_reader = csv.reader(problem_file)
        row = next(problem_reader)
        s, t = int(row[0]), int(row[1])
        problem = RoutingProblem(s, t)
        draw.plot_path(problem.roads, algs.find_astar_route(problem)[0])
        plt.show()
