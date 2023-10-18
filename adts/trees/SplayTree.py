from adts.atomize.Nodes import SplayNode
from adts.atomize.Types import Comparable

from adts.trees.ZigZag import ZigZag

from typing import Optional


class SplayTree(ZigZag):
    def __init__(self, root: SplayNode):
        super().__init__(root)
        self._len = 0

    def __len__(self):
        return self._len

    @staticmethod
    def leftOfParent(N: SplayNode) -> bool:
        return N == N.parent.left

    @staticmethod
    def rightOfParent(N: SplayNode) -> bool:
        return N == N.parent.right

    @staticmethod
    def leftOfGrand(N: SplayNode) -> bool:
        if N.parent is not None:
            return N.parent == N.parent.parent.left
        else:
            return False

    @staticmethod
    def rightOfGrand(N: SplayNode) -> bool:
        if N.parent is not None:
            return N.parent == N.parent.parent.right
        else:
            return False

    def splay(self, N: SplayNode):
        while N.parent is not None:
            if N.grand is None:
                if self.leftOfParent(N):
                    self.zig(N.parent)
                else:
                    self.zag(N.parent)
            elif self.leftOfParent(N) and self.leftOfGrand(N):
                self.zig(N.grand)
                self.zig(N.parent)
            elif self.rightOfParent(N) and self.rightOfGrand(N):
                self.zag(N.grand)
                self.zag(N.parent)
            elif self.leftOfParent(N) and self.rightOfGrand(N):
                self.zig(N.parent)
                self.zag(N.parent)
            else:
                self.zag(N.parent)
                self.zig(N.parent)

    def replace(self, U: SplayNode, V: SplayNode):
        if U.parent is None:
            self.root = V
        elif self.leftOfParent(U):
            U.parent.left = V
        else:
            U.parent.right = V

        if V is not None:
            V.parent = U.parent

    @staticmethod
    def subMax(U: SplayNode) -> SplayNode:
        while U.left is not None:
            U = U.left

        return U

    @staticmethod
    def subMin(U: SplayNode) -> SplayNode:
        while U.right is not None:
            U = U.right

        return U

    def insert(self, key: Comparable):
        Z: SplayNode = self.root
        P = SplayNode()

        while Z is not None:
            P = Z
            if Z.key > key:
                Z = Z.right
            else:
                Z = Z.left

        Z = SplayNode(key=key)
        Z.parent = P

        if P is None:
            self.root = Z
        elif P.key < Z.key:
            P.right = Z
        else:
            P.left = Z

        self.splay(Z)
        self._len += 1

    def find(self, key: Comparable) -> SplayNode | None:
        Z: SplayNode = self.root
        while Z is not None:
            if Z.key < key:
                Z = Z.left
            elif Z.key > key:
                Z = Z.right
            else:
                return Z

        return None

    def remove(self, key: Comparable):
        Z: SplayNode | None = self.find(key)
        if Z is None:
            return

        self.splay(Z)

        if Z.left is None:
            self.replace(Z, Z.right)
        elif Z.right is None:
            self.replace(Z, Z.left)
        else:
            Y: SplayNode = self.subMin(Z.right)
            if Y.parent != Z:
                self.replace(Y, Y.right)
                Y.right = Z.right
                Y.right.parent = Y

            self.replace(Z, Y)
            Y.left = Z.left
            Y.left.parent = Y

        self._len += 1

    def minimum(self):
        return self.subMin(self.root)

    def maximum(self):
        return self.subMax(self.root)
