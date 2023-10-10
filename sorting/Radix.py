from typing import List


class Radix(object):

    @staticmethod
    def paddingOrd(astr: str, idx: int):
        if len(astr) < (idx + 1):
            return 0

        return ord(astr[idx])

    @staticmethod
    def sort(seq: List[str], region: int) -> List[str]:
        """

        :param seq:
        :param region: max length to compare
        :return:
        """
        sortedArr: List[str] = [''] * len(seq)
        for no in range(region - 1, -1, -1):
            countArr = [0] * 128  # ASCII_RANGE
            # accumulate countArr
            for i in range(len(seq)):
                idx: int = Radix.paddingOrd(seq[i], no)
                countArr[idx] += 1

            # reduce count array
            for i in range(1, len(countArr)):
                countArr[i] += countArr[i - 1]

            # iter count array reversely and output
            for i in range(len(seq) - 1, -1, -1):
                idx: int = Radix.paddingOrd(seq[i], no)
                sortedIdx: int = countArr[idx] - 1
                sortedArr[sortedIdx] = seq[i]
                countArr[idx] -= 1

            seq = sortedArr[:]

        return seq


if __name__ == '__main__':
    array = ['qd', 'abc', 'qwe', 'hhh', 'a', 'cws', 'ope']
    print(Radix.sort(array, 3))
