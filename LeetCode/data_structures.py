from typing import Union
from collections import deque
import operator

class MinMaxQueue:
    def __init__(self, *args, type="min"):
        assert type in ["min", "max"], f"Only min and max are valid type for MinMaxQueue"
        self.min_max_type = type
        self.data = deque()
        self.queue = deque()
        self.compare = operator.lt if type == "min" else operator.gt
        if len(args) > 0:
            for n in args[0]:
                self.enqueue(n)
    
    def enqueue(self, n: Union[int, float]):
        self.data.append(n)
        while self.queue and self.compare(n, self.queue[-1]):
            self.queue.pop()
        self.queue.append(n)

    def dequeue(self):
        if self.data[0] == self.queue[0]:
            self.queue.popleft()
        return self.data.popleft()
    
    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"{repr(self.data)}, {repr(self.queue)}"

    def max(self):
        if self.min_max_type == "min":
            raise AttributeError("Can't call max when the type of the queue is min")
        try:
            return self.queue[0]
        except IndexError:
            raise ValueError("max() arg is an empty sequence")
    
    def min(self):
        if self.min_max_type == "max":
            raise AttributeError("Can't call min when the type of the queue is max")
        try:
            return self.queue[0]
        except IndexError:
            raise ValueError("min() arg is an empty sequence")
    