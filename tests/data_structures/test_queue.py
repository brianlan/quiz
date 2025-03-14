import pytest
from LeetCode.data_structures import MinMaxQueue

def test_max_queue_append_pop():
    queue = MinMaxQueue(type="max")
    with pytest.raises(ValueError):
        queue.max()
    with pytest.raises(AttributeError):
        queue.min()
    queue.enqueue(3)
    assert queue.max() == 3
    queue.enqueue(7)
    assert queue.max() == 7
    queue.enqueue(4)
    assert queue.max() == 7
    assert queue.dequeue() == 3
    queue.enqueue(5)
    assert len(queue) == 3
    assert queue.max() == 7
    assert queue.dequeue() == 7
    assert queue.max() == 5
    assert queue.dequeue() == 4
    assert queue.max() == 5
    assert queue.dequeue() == 5
    assert len(queue) == 0


def test_min_queue_append_pop():
    queue = MinMaxQueue(type="min")
    with pytest.raises(ValueError):
        queue.min()
    with pytest.raises(AttributeError):
        queue.max()
    queue.enqueue(3)
    assert queue.min() == 3
    queue.enqueue(7)
    assert queue.min() == 3
    queue.enqueue(4)
    assert queue.min() == 3
    assert queue.dequeue() == 3
    queue.enqueue(5)
    assert len(queue) == 3
    assert queue.min() == 4
    assert queue.dequeue() == 7
    assert queue.min() == 4
    assert queue.dequeue() == 4
    assert queue.min() == 5
    assert queue.dequeue() == 5
    assert len(queue) == 0


def test_max_queue_init_with_list():
    queue = MinMaxQueue([6, 7, 1, 8, 9, 4, 2], type="max")
    assert len(queue) == 7
    assert queue.max() == 9
    assert queue.dequeue() == 6
    queue.enqueue(6)
    assert queue.max() == 9
    assert queue.dequeue() == 7
    assert queue.max() == 9
    assert queue.dequeue() == 1
    assert queue.max() == 9
    assert queue.dequeue() == 8
    assert queue.max() == 9
    assert queue.dequeue() == 9
    assert queue.max() == 6
    queue.enqueue(5)
    assert queue.dequeue() == 4
    assert queue.max() == 6
    assert queue.dequeue() == 2
    assert queue.max() == 6
    assert queue.dequeue() == 6
    assert queue.max() == 5
    assert queue.dequeue() == 5
    with pytest.raises(ValueError):
        queue.max()
    with pytest.raises(IndexError):
        queue.dequeue()


def test_max_queue_bad_case1():
    q = MinMaxQueue([-7,-8,7,5], type="max")
    assert q.max() == 7
    assert q.dequeue() == -7
    assert q.max() == 7
    q.enqueue(7)
    assert q.max() == 7
    assert q.dequeue() == -8
    assert q.max() == 7
    q.enqueue(1)
    assert q.max() == 7
    assert q.dequeue() == 7
    assert q.max() == 7
    q.enqueue(6)
    assert q.max() == 7
    assert q.dequeue() == 5
    assert q.max() == 7
    q.enqueue(0)
    assert q.max() == 7
    assert q.dequeue() == 7
    assert q.max() == 6
    assert q.dequeue() == 1
    assert q.max() == 6
    assert q.dequeue() == 6
    assert q.max() == 0
    assert q.dequeue() == 0
    with pytest.raises(ValueError):
        assert q.max()
