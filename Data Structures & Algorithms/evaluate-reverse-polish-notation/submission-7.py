class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b + a)
            elif char == "-":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif char == "*":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b * a)
            elif char == "/":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(int(b / a))
            else:
                stack.append(char)

        return int(stack[0])