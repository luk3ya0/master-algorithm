from typing import List

from sorting.Merge import Merge


class Bucket(object):
    @staticmethod
    def sort(seq: List[float]) -> List[float]:
        maxEle, minEle = seq[0], seq[0]
        for ele in seq:
            if ele > maxEle:
                maxEle = ele

            if ele < minEle:
                minEle = ele

        region = maxEle - minEle
        bucketNum = len(seq)
        buckets = []
        for _ in range(bucketNum):
            buckets.append(list())

        # add element to every bucket
        for idx in range(len(seq)):
            bucketNo = int((seq[idx] - minEle) * (bucketNum - 1) / region)
            buckets[bucketNo].append(seq[idx])

        # sort every bucket
        for bucket in buckets:
            if len(bucket) > 1:
                Merge.sort(bucket, 0, len(bucket) - 1)

        # merge bucket one by one
        sortedArr: List[float] = [0.0] * len(seq)
        idx: int = 0
        for bucket in buckets:
            for ele in bucket:
                sortedArr[idx] = ele
                idx += 1

        return sortedArr


if __name__ == '__main__':
    sequence: List[float] = [4.12, 6.421, 0.0023, 3.0, 2.123, 8.122, 4.123, 10.09]
    print(sequence)
    print(Bucket.sort(sequence))
