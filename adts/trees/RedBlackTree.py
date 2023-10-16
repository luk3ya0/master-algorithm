from adts.atomize.Nodes import RBNode
from adts.atomize.Types import Comparable

from typing import Optional


class RedBlackTree(object):
    def __init__(self, root: RBNode):
        self.root: RBNode = root

    @staticmethod
    def parentOf(node: RBNode) -> Optional['RBNode']:
        if node is None:
            return None
        return node.parent

    @staticmethod
    def setBlack(node: RBNode):
        node.color = RBNode.BLACK

    @staticmethod
    def setRed(node: RBNode):
        node.color = RBNode.RED

    @staticmethod
    def isRed(node: RBNode):
        return node.color == RBNode.RED

    @staticmethod
    def isBlack(node: RBNode):
        return node.color == RBNode.BLACK

    @staticmethod
    def colorOf(node: RBNode):
        return node.color

    @staticmethod
    def setColor(node: RBNode, color: bool):
        node.color = color

    @staticmethod
    def successorOf(node: RBNode):
        # find the successor of current in in-order traversal
        inOrderNext: RBNode = node.right
        while inOrderNext.left is not None:
            inOrderNext = inOrderNext.left

        return inOrderNext

    def search(self, target: Comparable) -> Optional['RBNode']:
        current: RBNode = self.root
        while current is not None:
            if current.key < target:
                current = current.right
            elif current.key > target:
                current = current.left
            else:
                break

        return current

    #     p                       p
    #    /                       /
    #   x                       y
    #  / \                     / \
    # lx  y     ----->        x  ry
    #    / \                 / \
    #   ly ry               lx ly
    def leftRotate(self, x: RBNode):
        # 1. 将 y 的左子节点赋给x的右子节点, 并将 x 赋给 y 左子节点的父节点 (y 左子节点非空时)
        y: RBNode = x.left
        x.right = y.left

        if y.left is not None:
            y.left.parent = x

        # 2. 将 x 的父节点 p (非空时) 赋给 y 的父节点，同时更新 p 的子节点为 y (左或右)
        y.parent = x.parent

        if x.parent is None:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y

        # 3. 将 y 的左子节点设为 x, 将 x 的父节点设为 y
        y.left = x
        x.parent = y

    #        p                   p
    #       /                   /
    #      y                   x
    #     / \                 / \
    #    x  ry   ----->      lx  y
    #   / \                     / \
    #  lx rx                   rx ry
    def rightRotate(self, y: RBNode):
        # 1. 将 x 的右子节点赋给 y 的左子节点, 并将 y 赋给 x 右子节点的父节点 (x 右子节点非空时)
        x: RBNode = y.left
        y.left = x.right

        if x.right is not None:
            x.right.parent = y

        # 2. 将 y 的父节点 p (非空时) 赋给 x 的父节点, 同时更新 p 的子节点为 x (左或右)
        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.right:
                y.parent.right = x
            else:
                y.parent.left = x

        # 3. 将 x 的右子节点设为 y, 将 y 的父节点设为 x
        x.right = y
        y.parent = x

    def insert(self, value: Comparable):
        node = RBNode(key=value)

        current: Optional['RBNode'] = None  # parent of node
        x = self.root  # for searching down

        while x is not None:
            current = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = current

        if current is not None:
            if node.key < current.key:
                current.left = node
            else:
                current.right = node

        else:
            self.root = node

        self.insertFixUp(node)

    def insertFixUp(self, N: RBNode):
        pass

    def remove(self, value: Comparable):
        node: RBNode = self.search(target=value)