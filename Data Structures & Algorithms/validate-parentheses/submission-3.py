class Solution:
    def isValid(self, s: str) -> bool:
        s_pair = { '(':')', '{':'}', '[':']'}
        s_stack = deque()

        for char in s:
            if char in s_pair:
                s_stack.append(char)
            else:
                if not s_stack:
                    return False
                if s_pair[s_stack[-1]] != char:
                    return False
                s_stack.pop()
            

        return not s_stack
