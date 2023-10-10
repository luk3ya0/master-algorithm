from adts.atomize.Types import Comparable
from typing import List


class Shell(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        gap = len(seq) // 2
        while gap > 0:
            for i in range(gap, len(seq)):
                temp = seq[i]
                j = i
                while j >= gap and seq[j-gap] > temp:
                    seq[j] = seq[j-gap]
                    j -= gap

                seq[j] = temp

            gap = gap // 2

        return seq


if __name__ == '__main__':
    alist = [5, 3, 9, 12, 6, 1, 7, 2, 4, 11, 8, 10]
    print(alist)
    print(Shell.sort(alist))
