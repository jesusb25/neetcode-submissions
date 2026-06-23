class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""

        a, b = a[::-1], b[::-1]
        carry = 0

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = carry + digitA + digitB

            char = str(total % 2)
            res = char + res

            carry = 1 if total > 1 else 0
        
        if carry:
            res = str(carry) + res

        return res
