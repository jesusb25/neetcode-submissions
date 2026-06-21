class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # sliding window, min whites in window of size k


        left = 0
        right = k - 1
        whites = 0
        for i in range(k):
            if blocks[i] == "W":
                whites += 1
        
        res = whites
        while right < len(blocks) - 1:
            if blocks[left] == "W":
                whites -= 1
            left += 1
            right += 1
            if blocks[right] == "W":
                whites += 1
            res = min(res, whites)
        return res

