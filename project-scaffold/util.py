"""Small data structures used by the Pac-Man search algorithms."""

import heapq


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def isEmpty(self):
        return not self._items


class Queue:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop()

    def isEmpty(self):
        return not self._items


class PriorityQueue:
    """A min-priority queue with the update operation used by search."""

    def __init__(self):
        self._heap = []
        self._counter = 0

    def push(self, item, priority):
        entry = [priority, self._counter, item]
        self._counter += 1
        heapq.heappush(self._heap, entry)

    def pop(self):
        return heapq.heappop(self._heap)[2]

    def isEmpty(self):
        return not self._heap

    def update(self, item, priority):
        """Insert ``item``; duplicate entries are harmless for graph search."""
        self.push(item, priority)


def raiseNotDefined():
    raise NotImplementedError("This function is part of a later assignment task.")
