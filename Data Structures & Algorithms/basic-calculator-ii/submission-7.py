class Solution:
    def calculate(self, s: str) -> int:
        op = "+"
        num = 0
        stack = []
        s = s.replace(" ", "")

        for i, char in enumerate(s):
            # build num
            if char.isdigit():
                num = num * 10 + int(char)
            
            # if last num or op
            if i == len(s) - 1 or not char.isdigit():
                if op == "+":
                    stack.append(num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    stack.append(int(stack.pop() / num))
                else:
                    stack.append(-num)
                op = char
                num = 0
        return sum(stack)
                
