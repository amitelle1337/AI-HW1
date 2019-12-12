import csv

from my_files import algs
from my_files.routing_problem import RoutingProblem
from my_files.utils import avg_time

if __name__ == '__main__':
    probs = []
    with open('problems.csv', 'r') as problem_file:
        problem_reader = csv.reader(problem_file)
        for row in problem_reader:
            s, t = int(row[0]), int(row[1])
            problem = RoutingProblem(s, t, cost=avg_time)
            probs.append((s, t, len(algs.find_astar_route(problem)[0])))
        probs.sort(key=lambda p: p[2])

    with open('problems.csv', 'w+', newline='') as problem_file:
        problem_writer = csv.writer(problem_file)
        for p in probs:
            problem_writer.writerow([p[0], p[1]])
