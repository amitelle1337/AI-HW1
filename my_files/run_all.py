import csv
import matplotlib.pyplot as plt

from my_files import create_problems, write_results, print_solution_img, alg_mean_std


def plot_heu_to_real(filename: str):
    heu, real = [], []
    with open(filename, 'r') as results_file:
        results_reader = csv.reader(results_file)
        for row in results_reader:
            heu.append(row[0])
            real.append(row[1])
    plt.clf()
    plt.plot(heu, real)
    plt.show()


if __name__ == '__main__':
    create_problems.main()
    write_results.main()
    print_solution_img.main()
    alg_mean_std.main()
    plot_heu_to_real('results/AStarRuns.txt')
