class UnionFind(object):
    def __init__(self, size):
        self._elements = list(range(size))
        self._parents = list(range(size))
        self._height = [1 for _ in range(size)]  # rank to optimized searching

    def __len__(self):
        return len(self._elements)

    def find(self, p):
        assert 0 <= p < len(self)
        while p != self._parents[p]:
            self._parents[p] = self._parents[self._parents[p]]  # compress the height of tree
            p = self._parents[p]

        return self._parents[p]

    def isConnected(self, p, q) -> bool:
        return self.find(p) == self.find(q)

    def unionElement(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)

        if pRoot == qRoot:
            return

        if self._height[pRoot] < self._height[qRoot]:
            self._parents[pRoot] = qRoot
        elif self._height[qRoot] < self._height[pRoot]:
            self._parents[qRoot] = pRoot
        else:
            self._parents[qRoot] = pRoot
            self._height[qRoot] += 1
