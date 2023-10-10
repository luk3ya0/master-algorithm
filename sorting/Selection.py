from adts.atomize.Types import Comparable
from typing import List


class Selection(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        for i in range(len(seq) - 1):
            minIdx: int = i
            for j in range(i + 1, len(seq)):
                if seq[j] < seq[minIdx]:
                    minIdx = j

            if i != minIdx:
                seq[i], seq[minIdx] = seq[minIdx], seq[i]

        return seq
