from adts.atomize import TreeNode
from adts.atomize import Comparable
from adts.trees.BinaryTree import BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self, root: TreeNode):
        super().__init__(root)

    def search(self, target: Comparable):
        current = self.root
        while current is not None:
            if current.value < target:
                current = current.right
            elif current.value > target:
                current = current.left
            else:
                break

        return current

    def insert(self, target: Comparable):
        if self.root is None:
            self.root = TreeNode(target)
            return

        current, previous = self.root, None
        while current is not None:
            if current.value == target:
                return
            previous = current
            if current.value < target:
                current = current.right
            else:
                current = current.left

        node = TreeNode(target)
        if previous.value < target:
            previous.right = node
        else:
            previous.left = node

    def remove(self, target: Comparable):
        if self.root is None:
            return

        # locate the target value
        current, previous = self.root, None
        while current is not None:
            if current.value == target:
                break
            previous = current
            if current.value < target:
                current = current.right
            else:
                current = current.left

        # not found the target value
        if current is None:
            return

        # target node is of degree 0 or 1
        if current.left is None or current.right is None:
            successor = current.left or current.right
            if current != self.root:
                if previous.left == current:
                    previous.left = successor
                else:
                    previous.right = successor
            else:
                self.root = successor
        # target node is of degree 2
        else:
            # find the successor of current in in-order traversal
            inOrderNext: TreeNode = current.right
            while inOrderNext.left is not None:
                inOrderNext = inOrderNext.left
            self.remove(inOrderNext.value)
            current.value = inOrderNext.value


