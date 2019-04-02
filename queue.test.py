import pytest
from queue import Queue

queue = Queue()

def has_a_data_attribute():
    assert queue.data == []