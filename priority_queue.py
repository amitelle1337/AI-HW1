import heapq


class PriorityQueue:

    def __init__(self, f=lambda x: x):
        self.heap = []
        self.f = f
        self.items_set = set()

    def append(self, item):
        heapq.heappush(self.heap, (self.f(item), item))
        self.items_set.add(item)

    def extend(self, items):
        for item in items:
            self.append(item)

    def pop(self):
        if self.heap:
            item = heapq.heappop(self.heap)[1]
            self.items_set.remove(item)
            return item
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __len__(self):
        return len(self.heap)

    def __contains__(self, key):
        return key in self.items_set

    def __getitem__(self, key):
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    def __delitem__(self, key):
        try:
            self.items_set.remove(key)
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)

    def __repr__(self):
        return str(self.heap)
