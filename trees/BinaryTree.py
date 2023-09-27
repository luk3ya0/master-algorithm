from atomize.Nodes import TreeNode, Comparable


class BinaryTree(object):
    def __init__(self, root: TreeNode):
        self.root = root

    @staticmethod
    def preOrder(root: TreeNode | None):
        if root is None:
            return
        print(root.value)
        BinaryTree.preOrder(root=root.left)
        BinaryTree.preOrder(root=root.right)

    @staticmethod
    def inOrder(root: TreeNode | None):
        if root is None:
            return
        BinaryTree.inOrder(root=root.left)
        print(root.value)
        BinaryTree.inOrder(root=root.right)

    @staticmethod
    def postOrder(root: TreeNode | None):
        if root is None:
            return
        BinaryTree.postOrder(root=root.left)
        BinaryTree.postOrder(root=root.right)
        print(root.value)


