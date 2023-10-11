from adts.atomize.Errors import QueueUnderflow


class CircQueue(object):
    def __init__(self, capacity=8):
        self._elems = [0] * capacity
        self._head = 0
        self._len = 0
        self._cap = capacity

    @property
    def isEmpty(self):
        return self._len == 0

    def __len__(self):
        return self._len

    def peek(self):
        if self.isEmpty:
            raise QueueUnderflow("failed in peek")

        return self._elems[self._head]

    def dequeue(self):
        if self.isEmpty:
            raise QueueUnderflow("failed in dequeue")

        elem = self._elems[self._head]
        self._head = (self._head + 1) % self._cap
        self._len -= 1

        return elem

    def enqueue(self, elem):
        if self._len == self._cap:
            self.extend()

        self._elems[(self._head + self._len) % self._cap] = elem
        self._len += 1

    def extend(self):
        oldCap = self._cap
        self._cap *= 2
        newElems = [0] * self._cap
        for idx in range(oldCap):
            newElems[idx] = self._elems[(self._head + idx) % oldCap]

        self._elems, self._head = newElems, 0


if __name__ == '__main__':
    circQ = CircQueue()
    for i in range(16, 0, -1):
        circQ.enqueue(i)

    print(circQ.dequeue())
