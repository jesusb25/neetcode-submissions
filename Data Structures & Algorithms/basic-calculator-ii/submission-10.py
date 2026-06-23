class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"
        s = s.replace(" ", "")

        for i, char in enumerate(s):
            # char is digit
            if char.isdigit():
                num = num * 10 + int(char)

                # i is not the last we can continue otherwise operate
                if i != len(s) - 1:
                    continue
            
            # save sums for end
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            # prioritze * and /
            elif op == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))

            num = 0
            op = char
        return sum(stack)

            