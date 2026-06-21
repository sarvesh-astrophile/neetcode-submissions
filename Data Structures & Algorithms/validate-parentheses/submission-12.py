class Solution:
    def isValid(self, s: str) -> bool:
        close_dict = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in range(len(s)):
            if s[i] not in close_dict:
                stack.append(s[i])
            else:
                if stack and close_dict[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False


