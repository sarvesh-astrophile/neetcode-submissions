class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # init
        result = [0] * len(temperatures)

        # dec stack, if left > right pop and put the value
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return result