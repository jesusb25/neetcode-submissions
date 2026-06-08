class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prevTemp, prevIndex = stack.pop()
                result[prevIndex] = i - prevIndex
            
            stack.append((temp, i))
        return result