from collections import namedtuple

from typing import List, Tuple, Optional

namedEdge = namedtuple('NamedEdge', ['start', 'stop', 'weight'])


class Edge(namedEdge):
    def __lt__(self, other: Optional['Edge']):
        return self.weight < other.weight

    def __gt__(self, other: Optional['Edge']):
        return self.weight > other.weight

    def __eq__(self, other: Optional['Edge']):
        return self.weight == other.weight


class Matrix(object):
    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix

    def delRow(self, index):
        self._matrix.pop(index)

    def delCol(self, index):
        for row in self._matrix:
            row.pop(index)

    def addRow(self, withVal: int):
        self._matrix += [withVal] * len(self._matrix)

    def addCol(self, withVal: int):
        for row in self._matrix:
            row.append(withVal)

    def setEdge(self, between: Tuple[int, int], weight: int):
        self._matrix[between[0]][between[1]] = weight

    def getEdge(self, between: Tuple[int, int]):
        return self._matrix[between[0]][between[1]]

    def edgesFrom(self, start: int):
        row = self._matrix[start]

        return [Edge(start=start, stop=to, weight=weight) for to, weight in enumerate(row) if to != start]


class GraphAdjMatrix(object):
    def __init__(self,
                 vertexes: List[int] = None,
                 edges: List[Edge] = None,
                 directed: bool = False):
        if vertexes is None:
            vertexes = []
        if edges is None:
            edges = []

        self._vertexes = vertexes
        self._edges = edges
        self._directed = directed

        self._matrix = Matrix(matrix=[[0] * len(self) for _ in range(len(self))])
        for e in self._edges:
            self._matrix.setEdge(between=(e[0], e[1]), weight=e[2])

    def __len__(self):
        return len(self._vertexes)

    def addVertex(self, val):
        self._vertexes.append(val)
        self._matrix.addRow(withVal=0)
        self._matrix.addCol(withVal=0)

    def delVertex(self, index: int):
        if index > len(self):
            raise IndexError()
        self._vertexes.pop(index)
        self._matrix.delRow(index)
        self._matrix.delCol(index)

    def setEdge(self, car: int, cdr: int, weight: int = 1):
        if self.isInvalid(car) or self.isInvalid(cdr):
            raise IndexError()

        self._matrix.setEdge(between=(car, cdr), weight=weight)
        if not self._directed:
            self._matrix.setEdge(between=(cdr, car), weight=weight)

    def getEdge(self, car: int, cdr: int):
        return self._matrix.getEdge(between=(car, cdr))

    def delEdge(self, car: int, cdr: int):
        self.setEdge(car, cdr, 0)

    def addEdge(self, car: int, cdr: int):
        self.setEdge(car, cdr, 1)

    def isInvalid(self, index):
        return 0 > index or index > len(self)

    def edgesFrom(self, start: int) -> List[Edge]:
        return self._matrix.edgesFrom(start)


if __name__ == '__main__':
    pass
