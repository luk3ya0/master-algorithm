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
    def successor(node: RBNode) -> Optional['RBNode']:
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
        # 1. Assign the left child of y to the right child of x,
        # and assign x to the parent of the left child of y (when the left child of y is not empty).
        y: RBNode = x.left
        x.right = y.left

        if y.left is not None:
            y.left.parent = x

        # 2. Assign the parent of x, p (when not empty), to the parent of y,
        # and update the children of p to be y (left or right).
        y.parent = x.parent

        if x.parent is None:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y

        # 3. Set the left child of y to x, and the parent of x to y.
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
        # 1. Assign the right child of x to the left child of y,
        # and assign y to the parent of the right child of x (if the right child of x is not empty).
        x: RBNode = y.left
        y.left = x.right

        if x.right is not None:
            x.right.parent = y

        # 2. Assign y's parent p (when not empty) to x's parent,
        # and update p's children to x (left or right).
        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.right:
                y.parent.right = x
            else:
                y.parent.left = x

        # 3. Set the right child of x to y, and the parent of y to x.
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
        P: RBNode  # parent of N
        G: RBNode  # grandparent of N
        U: RBNode  # sibling of parent

        # The parent node exists and the color of the parent node is red
        while (self.parentOf(N) is not None) and self.isRed(self.parentOf(N)):
            P = self.parentOf(N)  # access the parent
            G = self.parentOf(P)  # access the grandparent

            if P == G.left:
                U = G.right

                # case 1:
                if U is not None and self.isRed(U):
                    self.setBlack(P)
                    self.setBlack(U)
                    self.setRed(G)

                    N = G  # fix up recursively

                    continue

                # case 2:
                if N == P.right:
                    self.leftRotate(P)
                    N, P = P, N  # flip between N and P for rightRotate

                # case 3:
                self.setBlack(P)
                self.setBlack(G)

                self.rightRotate(G)

            else:  # symmetric
                U = G.left

                # case 1:
                if U is not None and self.isRed(U):
                    self.setBlack(P)
                    self.setBlack(U)
                    self.setRed(G)

                    N = G  # fix up recursively

                    continue

                # case 2: 🌚 🌝 🌓
                if N == P.left:
                    self.rightRotate(P)
                    N, P = P, N  # flip between N and P for leftRotate

                # case 3:
                self.setBlack(P)  # is equal to setBlack for N
                self.setRed(G)

                self.leftRotate(G)

        self.setBlack(self.root)  # awaiting verification

    def remove(self, value: Comparable):
        node: RBNode = self.search(target=value)

        if all([node.left, node.right]):
            S: RBNode = self.successor(node)
            S.key = node.key
            node = S

        replacement: RBNode = node.left if node.left is not None else node.right

    @staticmethod
    def removeFixUP(N: RBNode, P: RBNode):
        pass
