from ways import info, compute_distance


def ordered_set(coll):
    return dict.fromkeys(coll).keys()


def avg_time(link) -> float:
    top_speed = info.SPEED_RANGES[info.TYPE_INDICES.index(link.highway_type)][1]
    return link.distance / top_speed


def est_time(junc1, junc2) -> float:
    top_speed = max([speed_range[1] for speed_range in info.SPEED_RANGES])
    return compute_distance(junc1.lat, junc1.lon, junc2.lat, junc2.lon) / top_speed


def path_cost(node) -> float:
    return node.path_cost
