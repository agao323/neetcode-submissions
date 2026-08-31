from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        TIME:
            30:26.50 - not too bad. 10 min thinking, 20 min coding
                        missed an edge case where words can equal
                        each other, shouldn't miss that in an
                        interview ideally

        we want to build a DAG and return a topological sort to build
        the correct lexicographical ordering.

        go through the list, comparing i and i + 1
        each comparison finds the first letter that's different
        letter[i] forms a directed edge to letter[i + 1]

        failure modes
            a single string doesn't tell us anything about the letters
            in the string, but we can just return that string because 
            it's a valid ordering by default

            if i + 1 is a prefix of i, that's always impossible
            so we return ""

            if we detect any cycles in the DAG, that means we can't
            build a valid ordering, so also return ""
        
        1. create a class to represent each node in the graph,
            which just contains the letter and the neighbors
        2. create a helper function to find the first difference
            between two words
        3. build a graph using the helper function to define edges
        4. use kahn's algo w/ indegrees to build an ordering
        5. if any cycles (indegrees remaining > 0), return "".
            otherwise, return the ordering
        """

        letters = set()
        for word in words:
            letters |= set([c for c in word])

        graph = {letter: [] for letter in letters}
        indeg = {letter: 0 for letter in letters}

        # build the graph
        for i in range(len(words) - 1):
            diff = self.firstDiff(words[i], words[i + 1])

            if diff == "UnexpectedError":
                print(diff)
                return ""
            if diff is None:
                return ""
            if diff == "":
                continue
            
            u, v = diff[0], diff[1]
            graph[u].append(v)
            indeg[v] += 1

        # apply kahn's algo
        result = ""
        queue = [k for k, v in indeg.items() if v == 0]
        while queue:
            cur = queue.pop()
            result += cur
            for neighbor in graph[cur]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == len(letters) else ""


    def firstDiff(self, word1, word2) -> Optional[str]:
        """
        If we have something like [ab, abc] that doesn't
        actually tell us anything

        We should return None for invalid ordering and
        empty string for no information
        """
        if len(word2) < len(word1) and word1[:len(word2)] == word2:
            return None
        
        if len(word1) < len(word2) and word2[:len(word1)] == word1:
            return ""
        
        if word1 == word2:
            return ""
        
        # no prefixes means there's at least one difference and
        # we don't need to worry about out of bounds errors
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                return word1[i] + word2[i]

        return "UnexpectedError"








