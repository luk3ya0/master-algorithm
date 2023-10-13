from typing import List, Dict, Tuple

from adts.atomize.Nodes import Vertex


class GraphAdjList(object):
    def __init__(self, edges: List[Tuple[Vertex, Vertex]]):
        self._list = Dict[Vertex, List[Vertex]]()
        for edge in edges:
            self.addVertex(edge[0])
            self.addVertex(edge[1])
            self.addEdge(edge[0], edge[1])

    def __len__(self):
        return len(self._list)

    def invalidEdge(self, car: Vertex, cdr: Vertex):
        return car not in self._list or cdr not in self._list or car == cdr

    def addVertex(self, vertex: Vertex):
        if vertex in self._list:
            return

        self._list[vertex] = List[Vertex]()

    def addEdge(self, car: Vertex, cdr: Vertex):
        if self.invalidEdge(car, cdr):
            raise ValueError()

        if cdr not in self._list[car]:
            self._list[car].append(cdr)
        if car not in self._list[cdr]:
            self._list[cdr].append(car)

    def vertexFrom(self, start: Vertex):
        return self._list[start]

    def delVertex(self, vertex: Vertex):
        if vertex not in self._list:
            raise ValueError()

        self._list.pop(vertex)
        for vertex in self._list:
            if vertex in self._list[vertex]:
                self._list[vertex].remove(vertex)

    def delEdge(self, car: Vertex, cdr: Vertex):
        if self.invalidEdge(car, cdr):
            raise ValueError()

        self._list[car].remove(cdr)
        self._list[cdr].remove(car)
