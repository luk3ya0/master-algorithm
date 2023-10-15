from adts.atomize.Types import Comparable
from adts.heaps.PrioQueue import PrioQueue
from adts.atomize.Nodes import HuffmanNode

from typing import List


class HuffmanTree(object):
    def __init__(self, weights: List[Comparable]):
        self._weights = weights
        self._wooding = PrioQueue()

        self.root = self.buildHuffman()

    def buildHuffman(self) -> HuffmanNode:
        for w in self._weights:
            self._wooding.enqueue(HuffmanNode(key=w))

        while len(self._wooding) > 1:
            left: HuffmanNode = self._wooding.dequeue()
            right: HuffmanNode = self._wooding.dequeue()

            rootW = left.key + right.key

            self._wooding.enqueue(HuffmanNode(key=rootW).withLeft(left).withRight(right))

        return self._wooding.dequeue()
