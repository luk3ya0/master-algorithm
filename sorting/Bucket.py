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
        buckets = [[]] * bucketNum

        # add element to every bucket
        for idx in range(len(seq)):
            bucketNo = int((seq[idx] - minEle) * bucketNum / region - 1)
            buckets[bucketNo].append(seq[idx])

        # sort every bucket
        for bucket in buckets:
            Merge.sort(bucket, 0, len(bucket))

        # merge bucket one by one
        sortedArr: List[float] = [0.0] * len(seq)
        idx: int = 0
        for bucket in buckets:
            for ele in bucket:
                sortedArr[idx] = ele
                idx += 1

        return sortedArr
