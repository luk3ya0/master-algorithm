from adts.graphs.GraphAdjMatrix import GraphAdjMatrix


class Kruskal(object):

    @staticmethod
    def span(graph: GraphAdjMatrix):
        vertexCount = len(graph)
        reachSet = [i for i in range(vertexCount)]
        spanning, edges = [], []

        for idx in range(vertexCount):
            for edge in graph.edgesFrom(start=idx):
                edges.append(edge)

        edges = sorted(edges, key=lambda ele: ele.weight)

        for e in edges:
            if reachSet[e.start] != reachSet[e.stop]:
                spanning.append(((e.start, e.stop), e.weight))

                if len(spanning) == vertexCount - 1:
                    break

                inV, outV = reachSet[e.start], reachSet[e.stop]
                for i in range(vertexCount):
                    if reachSet[i] == outV:
                        reachSet[i] = inV

        return spanning
