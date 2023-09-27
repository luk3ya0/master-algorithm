from atomize.Nodes import LinkedNode
from atomize.Types import Comparable


class LinkedStack(object):
    def __init__(self):
        self.top = LinkedNode()  # End sentinel

    def push(self, value: Comparable):
        self.top = LinkedNode(value, self.top)

    def pop(self) -> Comparable:
        result: Comparable = self.top.value

        if not self.top.end():
            self.top = self.top.following

        return result


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
