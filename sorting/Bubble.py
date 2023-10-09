from adts.atomize.Types import Comparable
from typing import List


class Bubble(object):
    @staticmethod
    def sort(seq: List[Comparable]) -> List[Comparable]:
        """
        :param seq: sequence
        :return:
        """
        for i in range(len(seq) - 1):
            for j in range(len(seq) - i - 1):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]

        return seq
