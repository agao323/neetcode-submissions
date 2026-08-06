class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        graph problem. detect cycle
            1. build the graph:
                {
                    node.val: [neighbors]
                    ...
                }
            2. run through graph:
                2a. track seen nodes
                2b. return False if any seen already

            0: [1,2]
            1: []
            2: [1]

            dfs from each node?
            0 -> 1 -> null, valid
            0 -> 2 -> 1 -> null, valid
            1 -> null, valid
            2 -> 1 -> null, valid
        """
        graph = {i: [] for i in range(numCourses)}
        for pre, post in prerequisites:
            graph[pre].append(post)
        
        for i in range(numCourses):
            neighbors = graph[i]
            for n in neighbors:
                seen = set([i])
                while neighbors:
                    if n in seen:
                        return False
                    seen.add(n)
                    neighbors = graph[n]
        
        return True



        

        
        