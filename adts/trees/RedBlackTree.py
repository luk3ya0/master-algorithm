from adts.atomize.Nodes import RBNode

from typing import Optional


class RedBlackTree(object):
    def __init__(self, root: RBNode):
        self.root: RBNode = root

    @staticmethod
    def parentOf(node: RBNode) -> Optional['RBNode']:
        if node is None:
            return None
        return node.parent
