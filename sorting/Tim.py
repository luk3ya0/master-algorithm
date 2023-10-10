from typing import List

from adts.atomize.Types import Comparable
from sorting.Insertion import Insertion


class Tim(object):
    MIN_RUN = 5

    @staticmethod
    def merge(merged: List[Comparable], start: int, middle: int, stop: int) -> List[Comparable]:
        leftLen = middle - start + 1
        rightLen = stop - middle

        leftArr = [0] * leftLen
        rightArr = [0] * rightLen

        for i in range(leftLen):
            leftArr[i] = merged[start + i]
        for j in range(rightLen):
            rightArr[j] = merged[middle + 1 + j]

        i, j, k = 0, 0, start

        while i < leftLen and j < rightLen:
            if leftArr[i] <= rightArr[j]:
                merged[k] = leftArr[i]
                i += 1
            else:
                merged[k] = rightArr[j]
                j += 1

            k += 1

        while i < leftLen:
            merged[k] = leftArr[i]

            k, i = k + 1, i + 1

        while j < rightLen:
            merged[k] = rightArr[j]

            k, j = k + 1, j + 1

        return merged

    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        # insertion sort piece of MIN_RUN size
        for i in range(0, len(seq), Tim.MIN_RUN):
            if (i + Tim.MIN_RUN - 1) < (len(seq) - 1):
                Insertion.sort(seq, i, i + Tim.MIN_RUN)
            else:
                Insertion.sort(seq, i, len(seq))

        # merge by step
        size = Tim.MIN_RUN
        while size < len(seq):
            left = 0
            while left < len(seq):
                middle = left + size - 1

                if middle > len(seq) - 1:  # avoiding overflow
                    break

                if (left + 2 * size - 1) < len(seq) - 1:
                    right = left + 2 * size - 1
                else:
                    right = len(seq) - 1

                Tim.merge(merged=seq, start=left, middle=middle, stop=right)

                left += 2 * size
            size *= 2

        return seq


if __name__ == '__main__':
    alist = list(range(100, -1, -1))
    print(Tim.sort(alist))
