from adts.atomize.Nodes import SplayNode, RBNode


class ZigZag(object):
    def __init__(self, root: SplayNode | RBNode):
        self.root = root

    #     p                       p
    #    /                       /
    #   x                       y
    #  / \                     / \
    # lx  y     ----->        x  ry
    #    / \                 / \
    #   ly ry               lx ly
    # left rotate
    def zag(self, x: RBNode | SplayNode):
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
    # right rotate
    def zig(self, y: RBNode | SplayNode):
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
