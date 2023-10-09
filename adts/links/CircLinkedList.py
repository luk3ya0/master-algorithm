from adts.atomize.Types import Comparable
from adts.atomize.Nodes import LinkedNode
from adts.atomize.Errors import LinkedListUnderflow

from typing import Optional


class CircLinkedList(object):
    def __init__(self):
        self._rear: Optional['LinkedNode'] = None

    @property
    def isEmpty(self):
        return self._rear is None

    def prepend(self, value: Comparable):
        node = LinkedNode(value)
        if self.isEmpty:
            node.following = node  # self circular
            self._rear = node
        else:
            node.following = self._rear.following
            self._rear.following = node

    def append(self, value: Comparable):
        self.prepend(value)
        self._rear = self._rear.following

    def pop(self) -> Optional['Comparable']:
        if self.isEmpty:
            raise LinkedListUnderflow("failed in ")
        node = self._rear.following
        if self._rear is node:  # self circular
            self._rear = None
        else:
            self._rear.following = node.following

        return node.value

