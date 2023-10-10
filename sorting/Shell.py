from adts.atomize.Types import Comparable
from typing import List


class Insertion(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        gap = len(seq)
        while gap > 1:
            gap = gap // 2
            for start in range(gap):
                for i in range(start + gap, len(seq) + 1, gap):
                    temp: int = seq[i]
                    j: int = i - gap
                    for j in range(i - gap, -1, -gap):
                        if seq[j] > temp:
                            seq[j + gap] = seq[j]

                    seq[j + gap] = temp
        return seq
