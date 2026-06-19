class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = -float('inf')
        digits = set()
        for i in range(10):
            digits.add(i * 100 + i * 10 + i)
        
        for i in range(2, len(num)):
            string = num[i - 2 : i + 1]
            if int(string) in digits and int(string) > largest:
                largest = int(string)
        
        if largest == 0:
            return "000"
        elif largest > -float('inf'):
            return str(largest)
        else:
            return ""