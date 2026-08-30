from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        build the graph
            node: [neighbors]
            neighbors here are all courses that must be taken first
        do top sort algo:
            finding 0 in-degree nodes, ie all keys in the dict
            that point to an empty list
            add these nodes to the result
            keep going until we have no nodes left or there are
            no more nodes that have neighbors
        """
        graph = {n: [] for n in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        result = []
        while True:
            can_take = [k for k, v in graph.items() if len(v) == 0]
            
            if len(can_take) == 0:
                if len(graph) > 0:
                    return []
                else:
                    break

            for course in can_take:
                del graph[course]
            
            for course in can_take:
                for k, v in graph.items():
                    if course in v:
                        v.remove(course)

            result.extend(can_take)

        return result
        

