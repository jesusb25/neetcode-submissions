class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left and right pointer
        # time O(n)
        # Space O(n)
        # edge cases
        alphanum_string = ''
        for char in s:
            if char.isalnum():
                alphanum_string += char.lower()
        if len(alphanum_string) <= 1:
            return True
        left = 0
        right = len(alphanum_string) - 1
        while left <= right:
            if alphanum_string[left] != alphanum_string[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        