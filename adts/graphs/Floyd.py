from typing import Dict, Set, List

from adts.graphs.GraphAdjMatrix import GraphAdjMatrix, Edge


class Floyd(object):
    @staticmethod
    def distance(graph: GraphAdjMatrix):
        for k in range(len(graph)):
            for i in range(len(graph)):
                for j in range(len(graph)):
                    if graph.getEdge(i, k) == float('inf') or graph.getEdge(k, j):
                        continue

                    graph.setEdge(car=i, cdr=j, weight=min(graph.getEdge(i, j),
                                                           graph.getEdge(i, k) + graph.getEdge(k, j)))
