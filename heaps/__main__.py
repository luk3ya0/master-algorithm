import path
import sys

# directory reach
directory = path.Path(__file__).abspath()

# setting path
sys.path.append(directory.parent.parent)

from wooding import BinaryTree

print(BinaryTree)
