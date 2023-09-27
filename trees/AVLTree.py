from atomize.Nodes import TreeNode
from atomize.Types import Comparable
from wooding.BinarySearchTree import BinarySearchTree


class AVLTree(BinarySearchTree):
    def __init__(self, root: TreeNode):
        super().__init__(root)

    @staticmethod
    def rightRotate(node: TreeNode | None) -> TreeNode | None:
        child = node.left
        grandchild = child.right
        child.right = node
        node.left = grandchild

        return child

    @staticmethod
    def leftRotate(node: TreeNode | None) -> TreeNode | None:
        child = node.right
        grandchild = child.left
        child.left = node
        node.right = grandchild

        return child

    @staticmethod
    def rotate(node: TreeNode | None) -> TreeNode | None:
        balanceFactor = node.balanceFactor
        # unbalanced node
        if abs(balanceFactor) > 1:
            # left unbalanced tree
            if balanceFactor > 0:
                # right rotate
                if node.left.balanceFactor >= 0:
                    AVLTree.rightRotate(node)
                # left rotate first and then right rotate
                else:
                    node.left = AVLTree.leftRotate(node.left)
                    return AVLTree.rightRotate(node)
            # right unbalanced tree
            else:
                # left rotate
                if node.right.balanceFactor <= 0:
                    AVLTree.leftRotate(node)
                # right rotate first and then left rotate
                else:
                    node.right = AVLTree.rightRotate(node.right)
                    return AVLTree.leftRotate(node)

        return node

    @staticmethod
    def insertAndBalance(node: TreeNode | None, target: Comparable) -> TreeNode:
        if node is None:
            return TreeNode(target)

        # find the right position to insert the new node
        if target < node.value:
            node.left = AVLTree.insertAndBalance(node.left, target)
        elif target > node.value:
            node.right = AVLTree.insertAndBalance(node.right, target)
        else:
            return node

        # re-balance the node
        return AVLTree.rotate(node)

    def insert(self, target: Comparable):
        self.root = AVLTree.insertAndBalance(self.root, target)

    @staticmethod
    def removeAndBalance(node: TreeNode | None, target: Comparable) -> TreeNode | None:
        if node is None:
            return node
        if target < node.value:
            node.left = AVLTree.removeAndBalance(node.left, target)
        elif target > node.value:
            node.right = AVLTree.removeAndBalance(node.right, target)
        else:
            if node.left is None or node.right is None:
                child = node.left or node.right
                if child is None:
                    return
                else:
                    node = child
            else:
                # find the successor of current in in-order traversal
                inOrderNext = node.right
                while inOrderNext.left is not None:
                    inOrderNext = inOrderNext.left
                # remove inOrderNext in right subtree of node
                node.right = AVLTree.removeAndBalance(node.right, inOrderNext.value)
                # replace value of node as inOrderNext's
                node.value = inOrderNext.value

        # re-balance the node finally
        return AVLTree.rotate(node)

    def remove(self, target: Comparable):
        self.root = AVLTree.removeAndBalance(self.root, target)
