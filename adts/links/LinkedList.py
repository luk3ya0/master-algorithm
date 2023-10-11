from adts.atomize.Nodes import LinkedNode
from adts.atomize.Types import Comparable
from adts.atomize.Errors import LinkedListUnderflow

from typing import Optional, Callable


class LinkedList(object):
    def __init__(self):
        self._head: Optional["LinkedNode"] = None

    @property
    def isEmpty(self):
        return self._head is None

    # DONE: prepend
    def prepend(self, value: Comparable):
        self._head = LinkedNode(value, self._head)

    # DONE: pop
    def pop(self) -> Comparable:
        if self.isEmpty:
            raise LinkedListUnderflow("failed to pop on empty linked list")
        result = self._head.value
        self._head = self._head.following

        return result

    # DONE: append
    def append(self, value: Comparable):
        if self.isEmpty:
            self._head = LinkedNode(value, None)
        else:
            current = self._head
            # scroll down to sentinel
            while current.following is not None:
                current = current.following

            current.following = LinkedNode(value)

    # DONE: popLast
    def popLast(self) -> Comparable:
        if self.isEmpty:
            raise LinkedListUnderflow("failed in popLast on empty linked list")

        current = self._head
        if current.following is None:
            value = current.value
            self._head = None

            return value
        while current.following.following is not None:
            current = current.following

        value = current.following.value

        return value

    # TODO: search or support __filter__
    def search(self, pred: Callable[[LinkedNode], bool]):
        current = self._head
        while current is not None:
            if pred(current):
                return current.value

            current = current.following

    # TODO: iter by iterator pattern of python build-in data model
    def values(self):
        current = self._head
        while current is not None:
            yield current.value
            current = current.following

    def filter(self, pred: Callable[[LinkedNode], bool]):
        current = self._head
        while current is not None:
            if pred(current):
                yield current.value

            current = current.following

    def __reversed__(self):
        node: Optional['LinkedNode'] = None
        while self._head is not None:
            current = self._head
            self._head = current.following
            current.following = node
            node = current

        self._head = node

        return self
