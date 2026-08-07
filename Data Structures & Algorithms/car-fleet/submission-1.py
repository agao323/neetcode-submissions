class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
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
        """
        if len(position) == 1:
            return 1

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, key=lambda car: car[0])
        
        iterations = [0] * len(cars)
        for j in range(len(cars)):
            pos, sp = cars[j]
            iterations[j] = float((target - pos) / sp)
        
        count = 1
        for k in range(1, len(iterations)):
            if iterations[k] < iterations[k - 1]:
                count += 1

        return count


