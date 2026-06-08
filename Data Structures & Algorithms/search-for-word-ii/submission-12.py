class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True


class Solution:
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        ROWS, COLS = len(board), len(board[0])

        # Build trie from word list
        root = TrieNode()
        for word in words:
            root.insert(word)

        result = []
        path = []
        visited = set()

        def dfs(row: int, col: int, node: TrieNode) -> None:
            if node.is_end:
                result.append("".join(path))
                node.is_end = False  # Prevent duplicate results

            for dr, dc in Solution.DIRS:
                r, c = row + dr, col + dc

                if not (0 <= r < ROWS and 0 <= c < COLS):
                    continue
                if (r, c) in visited:
                    continue

                child = node.children[ord(board[r][c]) - ord('a')]
                if not child:
                    continue

                path.append(board[r][c])
                visited.add((r, c))
                dfs(r, c, child)
                visited.discard((r, c))
                path.pop()

        # Kick off DFS from each cell that matches a trie root child
        for i in range(ROWS):
            for j in range(COLS):
                child = root.children[ord(board[i][j]) - ord('a')]
                if not child:
                    continue

                path.append(board[i][j])
                visited.add((i, j))
                dfs(i, j, child)
                visited.discard((i, j))
                path.pop()

        return result