from adts.atomize.Types import Comparable
from typing import List


class Insertion(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        for i in range(1, len(seq)):
            insertValue: int = seq[i]
            j = i - 1
            for j in range(i - 1, -1, -1):
                if insertValue < seq[j]:
                    seq[j + 1] = seq[j]
            seq[j + 1] = insertValue
        return seq
