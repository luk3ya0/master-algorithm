from adts.atomize.Types import Comparable

from typing import List


class Counting(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        maxEle, minEle = seq[0], seq[0]
        for ele in seq:
            if ele > maxEle:
                maxEle = ele

            if ele < minEle:
                minEle = ele

        region = maxEle - minEle
        countArr = [0] * (region + 1)

        for ele in seq:
            countArr[ele - minEle] += 1

        for idx in range(1, len(countArr)):
            countArr[idx] += countArr[idx - 1]

        sortedSeq = [0] * len(seq)
        for idx in range(len(seq) - 1, -1, -1):
            sortedSeq[countArr[seq[idx] - minEle] - 1] = seq[idx]
            countArr[seq[idx] - minEle] -= 1

        return sortedSeq


if __name__ == '__main__':
    sequence = list(range(10, 0, -1))
    print(Counting.sort(sequence))
