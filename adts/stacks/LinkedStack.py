from adts.atomize import LinkedNode
from adts.atomize import Comparable


class LinkedStack(object):
    def __init__(self):
        self.top = LinkedNode()  # End sentinel
        self._depth = 0

    def push(self, value: Comparable):
        self.top = LinkedNode(value, self.top)
        self._depth += 1

    def pop(self) -> Comparable:
        result: Comparable = self.top.value

        if not self.top.end():
            self.top = self.top.following

        self._depth -= 1

        return result

    @property
    def isEmpty(self):
        return self._depth == 0

    @property
    def depth(self):
        if self.top.end():
            return 0

        return self._depth

    @depth.setter
    def depth(self, value: int):
        self._depth = value


if __name__ == '__main__':
    linkedStackStr = LinkedStack()
    for s in "Phasers on stun!".split():
        linkedStackStr.push(s)

    while not linkedStackStr.top.end():
        print(linkedStackStr.pop())

    linkedStackInt = LinkedStack()
    for i in range(5):
        linkedStackInt.push(i)

    while not linkedStackInt.top.end():
        print(linkedStackInt.pop())
