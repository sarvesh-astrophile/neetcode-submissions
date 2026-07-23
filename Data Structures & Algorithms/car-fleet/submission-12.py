class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        car_data = list(zip(position, speed))
        car_data = sorted(car_data, reverse=True, key=lambda x: x[0])

        for p, s in car_data:
            t = (target - p) / s
            stack.append(t)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)