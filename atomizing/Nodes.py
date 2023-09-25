from typing import Optional

from atomizing.Types import Comparable


class LinkedNode(object):
    def __init__(self, value: Comparable = None, successor: Optional['LinkedNode'] = None):
        self.value = value
        self.successor: Optional["LinkedNode"] = successor

    def end(self) -> bool:
        return self.value is None and self.successor is None


class TreeNode(object):
    def __init__(self, value: Comparable):
        self.value = value
        self._height = 0
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None

    def withLeft(self, node: Optional["TreeNode"]) -> Optional["TreeNode"]:
        self.left = node

        return self

    def withRight(self, node: Optional["TreeNode"]) -> Optional["TreeNode"]:
        self.right = node

        return self

    @property
    def balanceFactor(self):
        leftHeight = 0 if self.left is None else self.left.height
        rightHeight = 0 if self.right is None else self.right.height

        return leftHeight - rightHeight

    @property
    def height(self):
        if not any([self.left, self.right]):
            self._height = 0
        else:
            leftHeight = 0 if self.left is None else self.left.height
            rightHeight = 0 if self.right is None else self.right.height
            self._height = max([leftHeight, rightHeight]) + 1

        return self._height


if __name__ == '__main__':
    nodeNo4 = TreeNode(4)
    nodeNo3 = TreeNode(3).withLeft(nodeNo4)
    nodeNo2 = TreeNode(2)
    nodeNo1 = TreeNode(1).withLeft(nodeNo2).withRight(nodeNo3)

    print(nodeNo1.height)
    print(nodeNo1.balanceFactor)
