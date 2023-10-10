from adts.atomize.Types import Comparable
from typing import List


class Insertion(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        step = len(seq)
        while step > 1:
            step = step // 2
            for start in range(step):
                for i in range(start + step, len(seq) + 1, step):
                    temp: int = seq[i]
                    j: int = i - step
                    for j in range(i - step, -1, -step):
                        if seq[j] > temp:
                            seq[j + step] = seq[j]

                    seq[j + step] = temp
        return seq
