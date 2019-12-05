from ways import info


def ordered_set(coll):
    return dict.fromkeys(coll).keys()


def avg_time(link):
    speed_range = info.SPEED_RANGES[info.TYPE_INDICES.index(link.highway_type)]
    avg_speed = (speed_range[1] - speed_range[0]) / 2
    return link.distance / avg_speed
