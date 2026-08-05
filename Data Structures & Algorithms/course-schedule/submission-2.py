class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        TIME: 54:04
            - took way too long to remember how to do this. 12 minutes to implement
            - most likely not the most efficient solution with removing sinks one at a time
            - implementation probably also inefficient
            - at least I beat 100% runtime and 100% memory somehow?
        
        looking at solutions
            - first DFS solution I proposed was correct, probably just implemented incorrectly
            - actual solution also correct (Kahn's algo), but just need indegree instead of separate graph
            - this was messy. definitely need to revisit this to practice Kahn's again, and also dfs version

        graph problem. detect cycle
            1. build the graph:
                {
                    node.val: [prereqs]
                    ...
                }
            2. remove sink nodes until there are none left
                2a. if we removed every node, we're good
                2b. if any remain, there's a cycle
            
            note: 42:20 is when I finally figured out (remembered) this algo
            0: [1,2]
            1: []
            2: [1]

            0: []
            1: [0,2]
            2: [0]
        """
        pre_graph = {i: [] for i in range(numCourses)}
        post_graph = {i: [] for i in range(numCourses)}
        for pre, post in prerequisites:
            pre_graph[post].append(pre)
            post_graph[pre].append(post)

        sinks = [k for k,v in pre_graph.items() if not v]
        while sinks:
            curr = sinks.pop(0)
            neighbors = post_graph[curr]
            for n in neighbors:
                pre_graph[n].remove(curr)
                if not pre_graph[n]:
                    sinks.append(n)
            del pre_graph[curr]
            
        if pre_graph:
            return False
        return True
            
            

        
        



        

        
        