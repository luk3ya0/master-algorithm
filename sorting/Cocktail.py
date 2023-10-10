from adts.atomize.Types import Comparable
from typing import List


class Cocktail(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        for i in range(len(seq) // 2):
            # from left to right
            isSorted: bool = True
            for j in range(i, len(seq) - i - 1):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
                    isSorted = False
            if isSorted:
                break

            # from right to left
            isSorted: bool = True
            for j in range(len(seq) - i - 1, i, -1):
                if seq[j] < seq[j - 1]:
                    seq[j], seq[j - 1] = seq[j - 1], seq[j]
                    isSorted = False
            if isSorted:
                break

        return seq
