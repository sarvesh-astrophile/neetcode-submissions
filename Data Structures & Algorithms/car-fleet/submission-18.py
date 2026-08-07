class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # init
        stack = []

        # zip the position and speed
        cars = list(zip(position, speed))

        # sort with postion
        cars.sort(key=lambda x: x[0], reverse=True)

        # group with stack and pop if back car take less time
        for p, s in cars:
            t = (target - p) / s
            stack.append(t)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
