class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        [1,2,3,4,5,6,7,8]

        if hand mod groupSize != 0, we can return false immediately
        [0,1,1,2,1,1,1,1]

        we can initialize an array of size max(card) and do a bucket count
        to see how many of each card we have.

        go through this array and decrement groups of size groupSize. we
        decrement by whatever value we see first and subtract that from
        the next groupSize - 1 elements

        if sum(array) is 0, we're good. otherwise return false

        O(max(card) * groupSize)
        """

        bucket = [0] * (max(hand) + 1)
        for h in hand:
            bucket[h] += 1
        
        for i in range(len(bucket) - groupSize + 1):
            if bucket[i] > 0:
                tmp = bucket[i]
                for j in range(i, i + groupSize):
                    bucket[j] -= tmp
        
        for b in bucket:
            if b != 0:
                return False
        return True
