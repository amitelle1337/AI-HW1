import csv
import random
from my_files import algs
from my_files.routing_problem import RoutingProblem
from ways import draw
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('../problems.csv', 'r', newline='') as problem_file:
        problem_reader = csv.reader(problem_file)
        rows = [row for row in problem_reader]
        for i in range(5):
            idx = random.randint(0, len(rows))
            row = rows.pop(idx)
            s, t = int(row[0]), int(row[1])
            problem = RoutingProblem(s, t)
            draw.plot_path(problem.roads, algs.find_astar_route(problem)[0])
            plt.savefig('sulotions_img/plot_{}_{}.png'.format(s, t))
            plt.clf()
