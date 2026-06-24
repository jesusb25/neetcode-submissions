class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        for i in range(len(digits)):
            if digits[i] + carry > 9:
                carry = 1
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
                return digits[::-1]
            
        if carry:
            digits.append(carry)
        return digits[::-1]
            
