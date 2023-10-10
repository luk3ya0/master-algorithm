from adts.atomize.Types import Comparable
from typing import List, Optional


class Insertion(object):
    @staticmethod
    def sort(seq: List[Comparable], start: Optional['int'] = None, stop: Optional['int'] = None) -> List[Comparable]:
        if start is None:
            start = 0
        if stop is None:
            stop = len(seq)

        for i in range(start + 1, stop):
            insertValue: int = seq[i]
            j = i - 1
            for j in range(i - 1, start - 1, -1):
                if insertValue < seq[j]:
                    seq[j + 1] = seq[j]
            seq[j] = insertValue
        return seq


if __name__ == '__main__':
    alist = list(range(15, 1, -1))
    print(alist)
    print(Insertion.sort(alist, 5, 11))
