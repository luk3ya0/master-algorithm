from CircLinkedList import CircLinkedList


class Josephus(CircLinkedList):
    def __init__(self, stop: int, start: int, step: int):
        super().__init__()
        for no in range(stop):
            self.append(no + 1)

        self.turn(start-1)

        while not self.isEmpty:
            self.turn(step-1)
            print(self.pop(), end=" -> " if not self.isEmpty else "\n")

    def turn(self, step):
        for _ in range(step):
            self._rear = self._rear.following
