from atomizing.Nodes import TreeNode, Comparable


class LinkedBinaryTree(object):
    def __init__(self, root: TreeNode):
        self.root = root

    @staticmethod
    def preOrder(root: TreeNode | None):
        if root is None:
            return
        print(root.value)
        LinkedBinaryTree.preOrder(root=root.left)
        LinkedBinaryTree.preOrder(root=root.right)

    @staticmethod
    def inOrder(root: TreeNode | None):
        if root is None:
            return
        LinkedBinaryTree.inOrder(root=root.left)
        print(root.value)
        LinkedBinaryTree.inOrder(root=root.right)

    @staticmethod
    def postOrder(root: TreeNode | None):
        if root is None:
            return
        LinkedBinaryTree.postOrder(root=root.left)
        LinkedBinaryTree.postOrder(root=root.right)
        print(root.value)


class BinarySearchTree(LinkedBinaryTree):
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
