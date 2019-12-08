from ways import info, compute_distance


def ordered_set(coll):
    return dict.fromkeys(coll).keys()


def avg_time(link):
    top_speed = info.SPEED_RANGES[info.TYPE_INDICES.index(link.highway_type)][1]
    return link.distance / top_speed


def est_time(node1, node2):
    top_speed = max([speed_range[1] for speed_range in info.SPEED_RANGES])
    return compute_distance(node1.lat, node1.lon, node2.lat, node2.lon) / top_speed
