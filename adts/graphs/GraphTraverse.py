from adts.graphs.GraphAdjList import GraphAdjList, Vertex
from adts.queues.CircQueue import CircQueue
from adts.stacks.LinkedStack import LinkedStack

from typing import List, Set


class GraphTraverse(object):
    @staticmethod
    def breathFirst(graph: GraphAdjList, start: Vertex) -> List[Vertex]:
        visited: Set[Vertex] = {start}
        sequence: List[Vertex] = []

        circQ = CircQueue()
        circQ.enqueue(start)
        while not circQ.isEmpty:
            current = circQ.dequeue()
            sequence.append(current)
            for vertex in graph.vertexFrom(start=current):
                if vertex in visited:
                    continue

                circQ.enqueue(vertex)
                visited.add(vertex)

        return sequence

    @staticmethod
    def depthFirst(graph: GraphAdjList, start: Vertex) -> List[Vertex]:
        visited: Set[Vertex] = {start}
        sequence: List[Vertex] = []

        linkedSt = LinkedStack()
        linkedSt.push((0, graph.vertexFrom(start)))
        sequence.append(start)
        while not linkedSt.isEmpty:
            i, vertexes = linkedSt.pop()
            if i < len(vertexes):
                current = vertexes[i]
                linkedSt.push((i+1, vertexes))
                if current not in visited:
                    sequence.append(current)
                    visited.add(current)

                    linkedSt.push((0, graph.vertexFrom(current)))

        return sequence
