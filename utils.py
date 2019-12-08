from ways import info


def ordered_set(coll):
    return dict.fromkeys(coll).keys()


def avg_time(link):
    top_speed = info.SPEED_RANGES[info.TYPE_INDICES.index(link.highway_type)][1]
    return link.distance / top_speed
