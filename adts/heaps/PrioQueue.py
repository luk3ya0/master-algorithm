from adts.atomize.Types import Comparable
from adts.atomize.Errors import PrioQueueError

from typing import List, Callable


class PrioQueue(object):
    def __init__(self, alist=None,
                 pred: Callable[[Comparable, Comparable], bool] = lambda cat, cdr: cat < cdr):
        """
        :param alist: initial elements
        :param pred: < min-heap > max-heap
        """
        if alist is None:
            alist = []
        self._elems: List[Comparable] = alist
        self.pred = pred
        if len(alist) > 0:
            self.heapify()

    @property
    def elems(self):
        return self._elems

    def __len__(self):
        return len(self._elems)

    def __getitem__(self, index) -> Comparable:
        return self._elems[index]

    def __setitem__(self, index, value: Comparable):
        self._elems[index] = value

    def __str__(self):
        return f"[{', '.join([str(i) for i in self._elems])}]"

    @property
    def isEmpty(self):
        return len(self._elems) == 0

    def heapify(self):
        start, stop = len(self._elems) // 2, len(self._elems)
        for hit in range(start, -1, -1):
            self.shiftDown(self._elems[hit], hit, stop)

    def dequeue(self):
        if self.isEmpty:
            raise PrioQueueError("failed in dequeue")
        elems, prior, last = self._elems, self.peek(), self._elems.pop()
        if len(elems) > 0:
            self.shiftDown(last, 0, len(elems))

        return prior

    def enqueue(self, elem: Comparable):
        self._elems.append(None)  # add a dummy element
        self.shiftUp(elem, len(self._elems) - 1)

    def peek(self):
        if self.isEmpty:
            raise PrioQueueError("failed in peek")
        return self._elems[0]

    def shiftDown(self, elem: Comparable, start, stop):
        elems, parent, child = self._elems, start, start * 2 + 1
        while child < stop:
            if child + 1 < stop and self.pred(elems[child + 1], elems[child]):  # compare left child and right one
                child += 1  # shift to left child
            if self.pred(elem, elems[child]):  # normal
                break
            elems[parent] = elems[child]  # shift elem[child] up

            parent, child = child, 2 * child + 1

        elems[parent] = elem

    def shiftUp(self, elem: Comparable, stop):
        elems, child, parent = self._elems, stop, (stop - 1) // 2
        while child > 0 and self.pred(elem, elems[parent]):
            elems[child] = elems[parent]

            child, parent = parent, (parent - 1) // 2

        elems[child] = elem


if __name__ == '__main__':
    queue = PrioQueue(alist=list(range(10)))
    print(queue)
    while not queue.isEmpty:
        print(queue[0])
        queue.dequeue()
        print(queue)
