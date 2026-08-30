from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        TIME:
            19:26 - time to solve initial implementation with very inefficient
                    neighbor removal
            32:03 - time to complete indegrees implementation
                    note: don't need to track visited nodes because cycles will
                    never be explored since their in-degree count will never
                    hit 0
        """

        """
        in-degree approach

        build course -> pre or pre -> course?
            pre -> course, so when we take a course we know which
            next ones should have their in-degrees decremented
        array of in-degrees that gets counted when we build graph
        create a queue of the initial 0 in-degrees
            go through each neighbor and decrement in-degree
            if neighbor in-degree is now 0, we add to queue
            continue until queue is empty
        if in-degree array sum is 0, we're good. otherwise return []
        """

        graph = {n: [] for n in range(numCourses)}
        indegrees = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1

        queue = deque([])
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        result = list(queue)
        while queue:
            cur = queue.popleft()
            for n in graph[cur]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)
                    result.append(n)
        
        return result if sum(indegrees) == 0 else []


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

        course_to_prereq = {n: [] for n in range(numCourses)}
        for course, prereq in prerequisites:
            course_to_prereq[course].append(prereq)
        
        prereq_to_course = {n: [] for n in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_to_course[prereq].append(course)

        result = []
        while True:
            can_take = [k for k, v in course_to_prereq.items() if len(v) == 0]
            
            if len(can_take) == 0:
                if len(course_to_prereq) > 0:
                    return []
                else:
                    break

            for course in can_take:
                del course_to_prereq[course]
            
            for course in can_take:
                for neighbor in prereq_to_course[course]:
                    course_to_prereq[neighbor].remove(course)

            result.extend(can_take)

        return result
        """

