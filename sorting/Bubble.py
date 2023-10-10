from adts.atomize.Types import Comparable
from typing import List


class Bubble(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        """
        :param seq: sequence
        :return:
        """
        lastExchangeIdx: int = 0
        sortedBorder: int = len(seq) - 1
        for i in range(len(seq) - 1):
            isSorted: bool = True
            for j in range(sortedBorder):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
                    isSorted = False
                    lastExchangeIdx = j

            sortedBorder = lastExchangeIdx
            if isSorted:
                break

        return seq
