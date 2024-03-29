import csv
from my_files.routing_problem import RoutingProblem
from my_files.utils import est_time, avg_time
from my_files import algs


def write_results(alg_name: str):
    if alg_name == 'ucs':
        file_name = 'results/UCSRuns.txt'
        alg = algs.find_ucs_route
    elif alg_name == 'astar':
        file_name = 'results/AStarRuns.txt'
        alg = algs.find_astar_route
    elif alg_name == 'idastar':
        file_name = 'results/IDAStarRuns.txt'
        alg = algs.find_idastar_route
    else:
        raise Exception('Invalid Algorithm')

    with open(file_name, 'w+', newline='') as result_file, open('problems.csv', 'r') as problem_file:
        problem_reader = csv.reader(problem_file)
        result_writer = csv.writer(result_file)
        lines = 0
        for row in problem_reader:
            s, t = int(row[0]), int(row[1])
            problem = RoutingProblem(s, t, cost=avg_time)
            if alg_name == 'astar' or alg_name == 'idastar':
                result_writer.writerow([est_time(problem[s], problem[t]), alg(problem)[1]])
            else:
                result_writer.writerow([alg(problem)[1]])
            lines += 1
            if alg_name == 'idastar' and lines is 10:
                break


def main():
    algs = ['ucs', 'astar', 'idastar']
    for alg in algs:
        write_results(alg)


if __name__ == '__main__':
    main()
