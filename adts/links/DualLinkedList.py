from adts.atomize.Nodes import DualLinkedNode
from adts.atomize.Types import Comparable
from adts.atomize.Errors import LinkedListUnderflow

from typing import Optional


class DualLinkedList(object):
    def __init__(self):
        self._head: Optional['DualLinkedNode'] = None
        self._tail: Optional['DualLinkedNode'] = None

    def prepend(self, value: Comparable):
        node = DualLinkedNode(value, preceding=None, following=self._head)
        if self._head is None:  # empty list
            self._head = node
        else:
            node.following.preceding = node

        self._head = node

    def append(self, value: Comparable):
        node = DualLinkedNode(value, preceding=self._tail, following=None)
        if self._head is None:
            self._head = node
        else:
            node.preceding.following = node

        self._tail = node

    def pop(self) -> Comparable:
        if self._head is None:
            raise LinkedListUnderflow("failed in DualLinkedList.pop")
        value = self._head.value
        self._head = self._head.following
        if self._head is not None:
            self._head.preceding = None

        return value

    def popLast(self) -> Comparable:
        if self._head is None:
            raise LinkedListUnderflow("failed in DualLinkedList.popLast")
        value = self._tail.value
        self._tail = self._tail.preceding
        if self._tail is None:
            self._head = None
        else:
            self._tail.following = None

        return value
