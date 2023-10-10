from adts.atomize.Types import Comparable

from typing import List


class Quick(object):
    @staticmethod
    def sort(seq: List[Comparable], start: int = None, stop: int = None) -> List[Comparable]:
        if not start:
            start = 0
        if not stop:
            stop = len(seq)

        if start >= stop:
            return seq

        pivot: int = Quick.partition(seq, start, stop)

        Quick.sort(seq, start, pivot - 1)
        Quick.sort(seq, pivot + 1, stop)

        return seq

    @staticmethod
    def partition(seq: List[Comparable], start: int, stop: int) -> int:

        pivotEle: Comparable = seq[start]
        mark: int = start
        for idx in range(start+1, stop):
            if seq[idx] < pivotEle:
                mark += 1
                seq[mark], seq[idx] = seq[idx], seq[mark]

        seq[start], seq[mark] = seq[mark], pivotEle

        return mark


if __name__ == '__main__':
    alist = list(range(15, 1, -1))
    print(Quick.sort(alist))
