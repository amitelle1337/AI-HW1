'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

# do NOT import ways. This should be done from other files
# simply import your modules and call the appropriate functions
from my_files import algs
from my_files.routing_problem import RoutingProblem
from my_files.utils import avg_time


def find_ucs_rout(source, target):
    'call function to find path, and return list of indices'
    problem = RoutingProblem(source, target, cost=avg_time)
    return algs.find_ucs_route(problem)[0]


def find_astar_route(source, target):
    'call function to find path, and return list of indices'
    problem = RoutingProblem(source, target, cost=avg_time)
    return algs.find_astar_route(problem)[0]


def find_idastar_route(source, target):
    'call function to find path, and return list of indices'
    problem = RoutingProblem(source, target, cost=avg_time)
    return algs.find_idastar_route(problem)[0]


def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    path = []
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv

    dispatch(argv)
