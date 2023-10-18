from adts.atomize.Nodes import RBNode
from adts.atomize.Types import Comparable

from adts.trees.ZigZag import ZigZag

from typing import Optional


class RedBlackTree(ZigZag):
    def __init__(self, root: RBNode):
        super().__init__(root)

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

    def insert(self, value: Comparable):
        # N: Current Node of Concern
        N = RBNode(key=value)

        # parent of N
        P: Optional['RBNode'] = None
        # temp node for searching down
        X = self.root

        while X is not None:
            P = X
            if N.key < X.key:
                X = X.left
            else:
                X = X.right

        N.parent = P

        if P is not None:
            if N.key < P.key:
                P.left = N
            else:
                P.right = N

        else:
            self.root = N

        self.fixAfterInsertion(N)

    def fixAfterInsertion(self, N: RBNode):
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
                    self.zag(P)
                    N, P = P, N  # flip between N and P for rightRotate

                # case 3:
                self.setBlack(P)
                self.setBlack(G)

                self.zig(G)

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
                    self.zig(P)
                    N, P = P, N  # flip between N and P for leftRotate

                # case 3:
                self.setBlack(P)  # is equal to setBlack for N
                self.setRed(G)

                self.zag(G)

        self.setBlack(self.root)  # awaiting verification

    def remove(self, value: Comparable):
        # N: Current Node of Concern
        N: RBNode = self.search(target=value)

        if all([N.left, N.right]):
            # S: Successor of N
            S: RBNode = self.successor(N)
            N.key = S.key
            N = S  # focus on the successor of N

        # RPL: abbreviation for replacement
        RPL: RBNode = N.left if N.left is not None else N.right
        if RPL is not None:
            RPL.parent = N.parent
            if N.parent is None:
                self.root = RPL
            elif N == N.parent.left:
                N.parent.left = RPL
            else:
                N.parent.right = RPL

            N.left, N.right, N.parent = None, None, None  # delete the focused N

            if self.isBlack(N):
                self.fixAfterDeletion(RPL)
        elif N.parent is None:
            self.root = None
        else:  # the N to delete has not child
            if self.isBlack(N):
                self.fixAfterDeletion(N)

            if N.parent is not None:
                if N == N.parent.left:
                    N.parent.left = None
                elif N == N.parent.right:
                    N.parent.right = None

                N.parent = None

    def fixAfterDeletion(self, N: RBNode):
        while N != self.root and self.isBlack(N):
            if N == N.parent.left:
                # Parent of N
                P: RBNode = N.parent
                # Sibling of N
                S: RBNode = N.parent.right

                if self.isRed(S):
                    self.setBlack(S)
                    self.setRed(P)
                    self.zag(P)

                    S = N.parent.right

                if self.isBlack(S.left) and self.isBlack(S.right):
                    self.setRed(S)
                    N = P  # fix up recursively
                else:
                    if self.isBlack(S.right):
                        self.setBlack(S.left)
                        self.setRed(S)
                        self.zig(S)

                        S = N.parent.right

                    self.setColor(S, self.colorOf(N))
                    self.setBlack(P)
                    self.setBlack(S.right)

                    self.zag(P)

                    N = self.root  # break up the loop

            else:  # symmetric
                # Parent of N
                P: RBNode = N.parent
                # Sibling of N
                S: RBNode = N.parent.left

                if self.isRed(S):
                    self.setBlack(S)
                    self.setRed(P)

                    self.zig(P)

                    S = P.left

                if self.isBlack(S.right) and self.isBlack(S.left):
                    self.setRed(S)

                    N = P
                else:
                    if self.isBlack(S.left):
                        self.setBlack(S.right)
                        self.setRed(S)

                        self.zag(S)

                        S = P.left

                    self.setColor(S, self.colorOf(P))
                    self.setBlack(P)
                    self.setBlack(S.left)

                    self.zig(P)

                    N = self.root  # break up the loop

        self.setBlack(N)
