class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(stack)
            if token.isdigit() or len(token) > 1:
                stack.append(int(token))
            else:
                num = stack.pop()
                if token == "+":
                    stack[-1] += num
                elif token == "*":
                    stack[-1] *= num
                elif token == "/":
                    num2 = stack.pop()
                    stack.append(int(num2 / num))
                else:
                    stack[-1] -= num
        return stack[-1]
        