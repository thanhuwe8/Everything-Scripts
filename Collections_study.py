# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:53:34 2024

@author: thanh
"""


def test():
    pass

# namedtuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
point = Point(2, 4)
print(point)
point.x
point.y

Person = namedtuple("Person", ["name", "job"])
Person("A", "tester")


# Stack and queue
from collections import deque
ticket_queue = deque()

# enqueue
ticket_queue.append("Jane")
ticket_queue.append("John")
ticket_queue.append("Linda")

# dequeue
ticket_queue.popleft() #first in first out

# initializer -> "iterable" (like a list) and "maxlen"
recent_files = deque(['core.py', 'README.md', "__init__.py"], maxlen = 3)
recent_files.appendleft("database.py")
recent_files

# study 2:
deque((1,2,3,4))
deque([1,2,3,4])
deque("abcd")

# extend an existing deque
numbers = deque([1,2])
numbers.extend([3,4,5])
print(numbers)

# extend left
numbers.extendleft([-1,-2,-3,-4,-5])
print(numbers)

numbers.insert(5,0)
numbers

'''
One difference between deque and list is that deque.pop() doesn’t support popping the item at a given index.
'''
numbers.count(5)

# rotate feature -> rotate last element to first element: This method rotates the deque n steps to the right.
ordinals = deque(['first', 'second', 'third'])
ordinals.rotate() # default value is one
ordinals

# this is linked list operation actually
ordinals = deque(['first', 'second', 'third'])
ordinals[1]
ordinals[0:2] # no slicing




