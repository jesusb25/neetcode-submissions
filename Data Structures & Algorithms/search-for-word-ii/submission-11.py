class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            i = ord(char) - ord('a')
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.end = True


class Solution:
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            root.insert(word)

        result: List[str] = []
        path: List[str] = []
        seen: set[tuple[int, int]] = set()

        def dfs(row: int, col: int, node: TrieNode) -> None:
            if node.end:
                result.append("".join(path))
                node.end = False

            for dr, dc in Solution.DIRS:
                r, c = row + dr, col + dc
                if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in seen:
                    continue
                i = ord(board[r][c]) - ord('a')
                child = node.children[i]
                if child:
                    path.append(board[r][c])
                    seen.add((r, c))
                    dfs(r, c, child)
                    seen.discard((r, c))
                    path.pop()

        for i in range(ROWS):
            for j in range(COLS):
                idx = ord(board[i][j]) - ord('a')
                child = root.children[idx]
                if child:
                    path.append(board[i][j])
                    seen.add((i, j))
                    dfs(i, j, child)
                    seen.discard((i, j))
                    path.pop()

        return result