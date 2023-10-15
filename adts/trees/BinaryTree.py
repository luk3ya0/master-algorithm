from adts.atomize.Nodes import TreeNode


class BinaryTree(object):
    def __init__(self, root: TreeNode):
        self.root = root

    @staticmethod
    def preOrder(root: TreeNode | None):
        if root is None:
            return
        print(root.key)
        BinaryTree.preOrder(root=root.left)
        BinaryTree.preOrder(root=root.right)

    @staticmethod
    def inOrder(root: TreeNode | None):
        if root is None:
            return
        BinaryTree.inOrder(root=root.left)
        print(root.key)
        BinaryTree.inOrder(root=root.right)

    @staticmethod
    def postOrder(root: TreeNode | None):
        if root is None:
            return
        BinaryTree.postOrder(root=root.left)
        BinaryTree.postOrder(root=root.right)
        print(root.key)


