import path
import sys

# directory reach
directory = path.Path(__file__).abspath()

# setting path
sys.path.append(directory.parent.parent)

from adts.trees import BinaryTree

print(BinaryTree)
