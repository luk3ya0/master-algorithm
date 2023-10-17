from typing import Optional

from adts.atomize.Types import Comparable


class LinkedNode(object):
    def __init__(self, value: Comparable = None, following: Optional['LinkedNode'] = None):
        self.value = value
        self.following: Optional["LinkedNode"] = following

    def end(self) -> bool:
        return self.value is None and self.following is None


class DualLinkedNode(object):
    def __init__(self,
                 value: Comparable = None,
                 preceding: Optional['DualLinkedNode'] = None,
                 following: Optional['DualLinkedNode'] = None):
        self.value = value
        self.following = following
        self.preceding = preceding


class TreeNode(object):
    def __init__(self, key: Comparable):
        self.key = key
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


class HuffmanNode(TreeNode):
    def __lt__(self, other: Optional['HuffmanNode']):
        return self.key < other.key

    def __gt__(self, other: Optional['HuffmanNode']):
        return self.key < other.key

    def __eq__(self, other: Optional['HuffmanNode']):
        return self.key == other.key

    def withLeft(self, node: Optional["HuffmanNode"]) -> Optional["HuffmanNode"]:
        self.left = node

        return self

    def withRight(self, node: Optional["HuffmanNode"]) -> Optional["HuffmanNode"]:
        self.right = node

        return self


class Vertex(object):
    def __init__(self, value: int):
        self.value = value

    def __int__(self):
        return self.value

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass


class RBNode(object):
    BLACK = True
    RED = False

    def __init__(self, key: Comparable):
        self.key = key
        self.left: Optional['RBNode'] = None
        self.right: Optional['RBNode'] = None
        self.parent: Optional['RBNode'] = None
        self.color = self.BLACK

    def isBlack(self):
        return self.BLACK

    def isRed(self):
        return not self.color


if __name__ == '__main__':
    nodeNo4 = TreeNode(4)
    nodeNo3 = TreeNode(3).withLeft(nodeNo4)
    nodeNo2 = TreeNode(2)
    nodeNo1 = TreeNode(1).withLeft(nodeNo2).withRight(nodeNo3)

    print(nodeNo1.height)
    print(nodeNo1.balanceFactor)

    print(all([nodeNo1, nodeNo2]))
