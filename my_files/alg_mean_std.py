import csv
import time
from my_files import algs
from statistics import stdev, mean
from my_files.routing_problem import RoutingProblem


def calc_mean_std(alg_name: str) -> (float, float):
    if alg_name == 'ucs':
        alg = algs.find_ucs_route
    elif alg_name == 'astar':
        alg = algs.find_astar_route
    elif alg_name == 'idastar':
        alg = algs.find_idastar_route
    else:
        raise Exception('Invalid Algorithm')

    results = []
    with open('../problems.csv', 'r', newline='') as problem_file:
        problem_reader = csv.reader(problem_file)
        for row in problem_reader:
            s, t = int(row[0]), int(row[1])
            problem = RoutingProblem(s, t)
            start = time.time()
            _ = alg(problem)
            end = time.time()
            results.append(end - start)
            if alg_name == 'idastar' and len(results) is 5:
                break
    return mean(results), stdev(results)


if __name__ == '__main__':
    print(calc_mean_std('idastar'))
