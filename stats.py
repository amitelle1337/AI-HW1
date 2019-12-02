'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''

from collections import namedtuple
from ways import load_map_from_csv, info


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])

    num_of_juncs = len(roads.values())

    num_of_links = 0
    max_links = float('-inf')
    min_links = float('inf')

    total_distance = 0
    max_distance = float('-inf')
    min_distance = float('inf')

    road_info_type_map = {}
    for road_type in info.ROAD_TYPES:
        road_info_type_map[road_type] = 0

    for j in roads.values():
        for link in j.links:
            road_info_type_map[info.ROAD_TYPES[link.highway_type]] += 1
            max_distance = max(max_distance, link.distance)
            min_distance = min(min_distance, link.distance)
            total_distance += link.distance

        j_links = len(j.links)
        max_links = max(max_links, j_links)
        min_links = min(min_links, j_links)
        num_of_links += j_links

    return {
        'Number of junctions': num_of_juncs,
        'Number of links': num_of_links,
        'Outgoing branching factor': Stat(max=max_links, min=min_links, avg=(num_of_links / num_of_juncs)),
        'Link distance': Stat(max=max_distance, min=min_distance, avg=(total_distance / num_of_links)),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': road_info_type_map,  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print_stats()
