from adts.queues.CircQueue import CircQueue
from adts.stacks.LinkedStack import LinkedStack


class Maze(object):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self, matrix=None):
        if matrix is None:
            matrix = []
        self._maze = matrix

    def bfsPath(self, start, stop):
        if start == stop:
            print("Path found.")
            return

        circQ = CircQueue()
        self.mark(start)
        circQ.enqueue(circQ)
        while not circQ.isEmpty:
            pos = circQ.dequeue()
            for i in range(4):
                nextp = (pos[0] + Maze.dirs[i][0],
                         pos[1] + Maze.dirs[i][1])

                if self.passable(nextp):
                    if nextp == stop:
                        print("Path found.")
                        return

                    self.mark(nextp)
                    circQ.enqueue(nextp)

        print("Not path found.")

    def dfsPath(self, start, stop):
        if start == stop:
            print(start)
            return
        linkedSt = LinkedStack()
        self.mark(start)
        linkedSt.push((start, 0))
        while not linkedSt.isEmpty:
            pos, nxt = linkedSt.pop()
            for i in range(nxt, 4):
                nextp = (pos[0] + Maze.dirs[i][0],
                         pos[1] + Maze.dirs[i][1])
                if nextp == stop:
                    print(pos, "->", stop)
                    return

                if self.passable(nextp):
                    linkedSt.push((pos, i + 1))
                    self.mark(nextp)
                    linkedSt.push((nextp, 0))
                    break

        print("Not path found.")

    def dfsRecurPath(self, pos, stop) -> bool:
        self.mark(pos)
        if pos == stop:
            print(pos, end=" ")
            return True

        for i in range(4):
            nextp = pos[0] + Maze.dirs[i][0], pos[1] + Maze.dirs[i][1]
            if self.passable(pos=nextp):
                if self.dfsRecurPath(nextp, stop):
                    print(pos, end=" ")
                    return True

        return False

    def mark(self, pos):
        self._maze[pos[0]][pos[1]] = 2

    def passable(self, pos):
        return self._maze[pos[0]][pos[1]] == 0
