class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        TIME: 53:17.21
            again, pretty atrocious time, but had no help and did not check
            hints whatsoever. pretty happy I was able to solve this entirely
            on my own without looking at a solution.

        [4, 1, 0, 7]
        [6, 3, 1, 8]
        [8, 5, 2, 9]
        [10, 7, 3, 10]
        [10, 9, 4, 10]

        [0, 1, 2, 6, 7], [1, 4, 3, 2, 1], target = 20
        [5, 5, 8, 8]
        [8, 8, 9, 9]
        [10, 10, 10, 10]

        (20 - 0) / 1 = 20
        (20 - 1) / 4 = 4.75
        (20 - 2) / 3 = 6
        (20 - 6) / 2 = 7
        (20 - 7) / 1 = 13
        
        sort positions into ascending order, so we know which cars can't pass
        combine position and speed into tuples beforehand, so we don't lose track
        [(4, 2), (1, 2), (0, 1), (7, 1)]
        [(0, 1), (1, 2), (4, 2), (7, 1)]

        can we be more efficient that just doing position * speed until 
        everyone hits the target?

        whenever position[i] = position[i + 1], assign node at
        position[i]'s parent to be position[i + 1]

        if position[i + 1] was already equal to target, don't link them

        at the end, count the number of nodes with no parent

        can we figure out if an intersection occurs in O(1) time?
            target / speed = number of iterations
            position + target / speed?
            (10 / 1 + 0), (1 + 10 / 2), (4 + 10 / 2), (7 + 10 / 1)
        ->  10, 6, 9, 17

        target - position = remaining distance
        remaining distance / speed = # of iterations
        if # of iterations for i - 1 > i, it will never catch up

        [(0, 1), (1, 2), (4, 2), (7, 1)]
        ((10 - 0) / 1) = 10 iterations
        ((10 - 1) / 2) = 4.5, round up to 5
        ((10 - 4) / 2) = 3
        ((10 - 7) / 1) = 3


        create a node class to represent each car
            - value = index, just to track the car
            - position = original position
            - speed = speed
            - parent pointer

        seems like an uptree problem, count the number of connected pieces?

        algorithm:
            - sort by position into tuples of (position, speed)
            - calculate iterations for each one
            - go through and count number of ascending groups

        [0,4,2], [2,1,3]
        [2,6,7]
        [4,10,10]

        [(0,2), (2,4), (4,3)] target = 10
        10 / 2, 8 / 4, 6 / 3
        5, 4, 2

        forgot about the passing thing.
        work backwards instead?
        a new fleet only appears before index z if the iteration
        count is greater than iterations[z]

        """
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        # if len(position) == 1:
        #     return 1

        # # uses the first index to sort anyways
        # cars = sorted([(p, s) for p, s in zip(position, speed)])
        
        # iterations = [0] * len(cars)
        # for j in range(len(cars)):
        #     p, s = cars[j]
        #     iterations[j] = float((target - p) / s)

        # # print(cars)
        # # print(iterations)
        # count = 1
        # curr_max = iterations[-1]
        # for k in range(len(iterations) - 2, -1, -1):
        #     if iterations[k] > curr_max:
        #         count += 1
        #         curr_max = iterations[k]

        # return count


