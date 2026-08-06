from collections import defaultdict

class TimeMap:
    """
    {
        "alice": [("happy", 1), ("sad", 3)]
    }
    hashmap + binary search
    """

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        lookup the key, append to the list
        """
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        """
        if key not found, return ""
        otherwise bin search on list
            - potential gotcha: bin search shouldn't look for an exact match
            - just need to find the point where timestamp is greater than
              timestamp in the list
        """
        if key not in self.store:
            return ""
        
        return self.binary_search(self.store[key], timestamp)
    
    def binary_search(self, values: list[(str, int)], timestamp: int) -> int:
        """
        returns the index of the element we want

        we want to find the first element in values that is strictly less
        than timestamp. so if arr[mid] > timestamp, we should keep looking,
        and if arr[mid] < timestamp, we also keep looking.

        if arr[mid] > timestamp and arr[mid - 1] < timestamp, we're done

        edge cases: first and last elements?
        """
        if len(values) == 0:
            # shouldn't be possible
            return ""
        
        if len(values) == 1:
            if timestamp < values[0][1]:
                # the only element is past the timestamp we want, 
                # so return nothing
                return ""
            return values[0][0]

        l, r = 0, len(values) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            curr = values[mid]
            prev = values[mid - 1]

            if curr[1] == timestamp:
                return curr[0]

            if prev[1] < timestamp < curr[1]:
                return prev[0]

            if curr[1] > timestamp:
                r = mid - 1
            if curr[1] < timestamp:
                l = mid + 1
            
        if l >= len(values):
            return values[-1][0]
        return ""












        
