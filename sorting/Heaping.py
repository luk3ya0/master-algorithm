from adts.atomize.Types import Comparable
from adts.heaps.PrioQueue import PrioQueue
from typing import List


class Heaping(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        """ in-place heap sort
        :param seq: sequence
        :return:
        """
        heapified = PrioQueue(alist=seq, pred=lambda car, cdr: car > cdr)
        stop = len(heapified)
        for hit in range(stop - 1, 0, -1):
            last = heapified[hit]
            heapified[hit] = heapified.peek()
            heapified.shiftDown(last, start=0, stop=hit)
        return heapified.elems


if __name__ == '__main__':
    alist = list(range(15, -1, -1))
    print(alist)
    alist = Heaping.sort(alist)
    print(alist)
