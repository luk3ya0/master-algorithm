from typing import List

from adts.atomize.Types import Comparable


class Merge(object):
    @staticmethod
    def sort(seq: List[Comparable], start: int, stop: int) -> List[Comparable]:
        if start < stop:
            middle: int = (start + stop) // 2
            Merge.sort(seq, start, middle)
            Merge.sort(seq, middle + 1, stop)

            return Merge.merge(seq, start, middle, stop)

    @staticmethod
    def merge(merged: List[Comparable], start: int, middle: int, stop: int) -> List[Comparable]:
        merging: List[Comparable] = list()
        p1, p2, p3 = start, middle + 1, 0
        while p1 <= middle and p2 <= stop:
            if merged[p1] <= merged[p2]:
                merging[p3] = merged[p1]
                p1, p3 = p1 + 1, p3 + 1
            else:
                merging[p3] = merged[p2]
                p2, p3 = p2 + 1, p3 + 1

        while p1 <= middle:
            merging[p3] = merged[p1]
            p1, p3 = p1 + 1, p3 + 1

        while p2 <= stop:
            merging[p3] = merged[p2]
            p2, p3 = p2 + 1, p3 + 1

        return merging
