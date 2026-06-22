class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = sum(1 if block == "W" else 0 for block in blocks[:k])
        res = whites

        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                whites += 1
            if blocks[i - k] == "W":
                whites -= 1
            
            res = min(whites, res)
        return res

        