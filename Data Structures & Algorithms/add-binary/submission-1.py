class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digit1 = int(a[i]) if i < len(a) else 0
            digit2 = int(b[i]) if i < len(b) else 0

            total = digit1 + digit2 + carry
            print(f"digit1: {digit1}, digit2: {digit2}, carry: {carry}")
            carry = total // 2
            
            char = str(total % 2) # 3 or 1 gives you 1
            res = char + res
        
        if carry:
            res = "1" + res
        return res
        

            




        