class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        dec_stack = [] # index

        for i in range(len(temperatures)):
            while dec_stack and temperatures[dec_stack[-1]] < temperatures[i]:
                index = dec_stack[-1]
                result[index] = i - index
                dec_stack.pop()

            dec_stack.append(i)

        return result