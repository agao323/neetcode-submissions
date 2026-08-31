class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        a triplet can be considered if one or more of its values equals the
        target values, and the other ones are not greater than the other
        target values

        if we can fill all three slots this way, we can return true
        """

        slots = [False] * 3

        for a, b, c in triplets:
            if a == target[0] and b <= target[1] and c <= target[2]:
                slots[0] = True
            if a <= target[0] and b == target[1] and c <= target[2]:
                slots[1] = True
            if a <= target[0] and b <= target[1] and c == target[2]:
                slots[2] = True
        
        return all(slots)

