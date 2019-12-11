import csv
from routing_problem import RoutingProblem
from utils import est_time
import algs


def write_results(alg_name: str):
    if alg_name == 'ucs':
        file_name = 'results/UCSRuns.txt'
        alg = algs.find_ucs_route
        heuristic = False
    elif alg_name == 'astar':
        file_name = 'results/AStarRuns.txt'
        alg = algs.find_astar_route
        heuristic = True
    elif alg_name == 'idastar':
        file_name = 'results/IDAStarRuns.txt'
        alg = algs.find_idastar_route
        heuristic = True
    else:
        raise Exception('Invalid Algorithm')

    with open(file_name, 'w+') as result_file, open('problems.csv', 'r', newline='') as problem_file:
        problem_reader = csv.reader(problem_file)
        for row in problem_reader:
            s, t = int(row[0]), int(row[1])
            problem = RoutingProblem(s, t)
            if heuristic:
                output_row = '{}, {}\n'.format(est_time(problem[s], problem[t]), alg(problem)[1])
            else:
                output_row = '{}\n'.format(alg(problem)[1])
            result_file.write(output_row)


if __name__ == '__main__':
    write_results('ucs')
    write_results('astar')
    write_results('idastar')
