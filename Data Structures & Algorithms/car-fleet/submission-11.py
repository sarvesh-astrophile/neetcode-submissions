class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair = sorted(pair, reverse=True, key=lambda k: k[0])
        stack = []

        for p, s in pair:
            t = (target - p) / s
            stack.append(t)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
