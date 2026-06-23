class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"
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

            
            num = 0
            op = char
        return sum(stack)

            