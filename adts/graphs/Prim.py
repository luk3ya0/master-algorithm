from adts.graphs.GraphAdjMatrix import GraphAdjMatrix
from adts.queues.CircQueue import CircQueue


class Prim(object):

    @staticmethod
    def span(graph: GraphAdjMatrix):
        vertexCount = len(graph)
        spanning = [None] * vertexCount
        candidates = CircQueue((0, 0, 0))
        vectorCount = 0

        while vectorCount < vertexCount and not candidates.isEmpty:
            w, u, v = candidates.dequeue()
            if spanning[v]:
                continue

            spanning[v] = ((u, v), w)
            vectorCount += 1
            for e in graph.edgesFrom(v):
                if not spanning[e.stop]:
                    candidates.enqueue((e.weight, e.start, e.stop))

        return spanning
