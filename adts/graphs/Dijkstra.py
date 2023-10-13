from typing import Dict, Set, List

from adts.graphs.GraphAdjMatrix import GraphAdjMatrix, Edge


class Dijkstra(object):
    @staticmethod
    def distance(graph: GraphAdjMatrix, initial: int) -> Dict[int, int]:
        distanceMap: Dict[int, int | float] = dict()
        preceding: Dict[int, int] = dict()  # stop vertex and preceding vertex in most short path

        visitedSet: Set[int] = {initial}
        size = len(graph)

        for i in range(size):
            if i != initial:
                distanceMap[i] = float('inf')

        edges: List[Edge] = graph.edgesFrom(start=initial)

        for edge in edges:
            distanceMap.update({edge.stop: edge.weight})
            preceding.update({edge.stop: -1})

        for i in range(1, size):  # vertexes except initial one
            minDistanceFromStart = float('inf')
            minDistanceIndex = -1

            for j in [idx for idx in range(size) if idx != initial]:  # vertexes except initial one
                if j not in visitedSet and distanceMap.get(j) < minDistanceFromStart:
                    minDistanceFromStart = distanceMap.get(j)
                    minDistanceIndex = j

            if minDistanceIndex == -1:
                break

            visitedSet.add(minDistanceIndex)
            for edge in graph.edgesFrom(minDistanceIndex):
                if edge.stop in visitedSet:
                    continue

                weight = edge.weight
                prevWeight = distanceMap.get(edge.stop)
                if weight != float('inf') and (minDistanceFromStart + weight) < prevWeight:
                    distanceMap.update({edge.stop: minDistanceFromStart + weight})
                    preceding[edge.stop] = minDistanceIndex

        return distanceMap


if __name__ == '__main__':
    print(float('inf') > 1)
