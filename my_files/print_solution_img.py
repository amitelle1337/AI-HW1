import csv
import random
from my_files import algs
from my_files.routing_problem import RoutingProblem
from my_files.utils import avg_time
from ways import draw
import matplotlib.pyplot as plt


def main():
    with open('problems.csv', 'r') as problem_file:
        problem_reader = csv.reader(problem_file)
        rows = [row for row in problem_reader]
        for i in range(5):
            idx = random.randint(0, len(rows) - 1)
            row = rows.pop(idx)
            s, t = int(row[0]), int(row[1])
            problem = RoutingProblem(s, t, cost=avg_time)
            plt.clf()
            draw.plot_path(problem.roads, algs.find_astar_route(problem)[0])
            plt.title('{} to {}'.format(s, t))
            plt.savefig('sulotions_img/plot_{}.png'.format(i))


if __name__ == '__main__':
    main()
