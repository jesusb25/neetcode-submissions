class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        op = "+"

        stack = []
        s = s.replace(" ", "")

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
                if i != len(s) - 1:
                    continue
                
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            op = char
            num = 0
        return sum(stack)