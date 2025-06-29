from typing import *


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        combined = []
        for i in range(n):
            combined.append((position[i], speed[i]))

        combined.sort(key=lambda x: x[0])
        times = [0] * n
        for i, elem in enumerate(combined):
            pos, speed = elem
            times[i] = (target - pos) / speed

        mdStack = []
        for time in times:
            while mdStack and time > mdStack[-1]:
                mdStack.pop()
            mdStack.append(time)

        return len(mdStack)


s = Solution()
print(s.carFleet(10, [0, 1, 2, 4], [12, 5, 2, 3]))
