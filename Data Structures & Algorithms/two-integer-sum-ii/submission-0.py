class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):

            left = i + 1
            right = len(numbers) - 1
            complement = target - num

            while left <= right:
                middle = left + (right - left) // 2

                if numbers[middle] == complement:
                    return [i + 1, middle + 1]
                elif numbers[middle] < complement:
                    left = middle + 1
                else:
                    right = middle - 1

        return [0,0]