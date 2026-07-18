class Solution:
    def isValid(self, s: str) -> bool:
        starttoend = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in starttoend:
                stack.append(starttoend[char])
            elif stack and char == stack[-1]:
                stack.pop()
            else:
                return False

        return True if not stack else False
