class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Solution:
    def insertWord(self, word):
        # insert word into tree
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.end = True
    


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # turn all words into a trie
        # navigate only if neigbors contain a enxt letter
        ROWS = len(board)
        COLS = len(board[0])
        self.root = TrieNode()
        seen = set()
        result = []
        path = []

        # turn all words into a single word tree
        for word in words:
            self.insertWord(word)
        
        def dfs(row, col, node):
            # if node is end of word, mark the word in result
            if node.end:
                result.append("".join(path))
                node.end = False

            # then get neighbors, only explore neighbors where trienodes exist
            neighbors = [
                (row + 1, col),
                (row, col + 1),
                (row - 1, col),
                (row, col - 1),
            ]

            for new_row, new_col in neighbors:
                if (min(new_row, new_col) < 0 or 
                new_row == ROWS or
                new_col == COLS or
                (new_row, new_col) in seen):
                    continue
                
                next_char = board[new_row][new_col]
                next_index = ord(next_char) - ord('a')
                next_node = node.children[next_index]
                if next_node:
                    path.append(next_char)
                    seen.add((new_row,new_col))
                    dfs(new_row, new_col, next_node)
                    seen.remove((new_row,new_col))
                    path.pop()

        for i in range(ROWS):
            for j in range(COLS):
                char = board[i][j]
                index = ord(char) - ord('a')
                start = self.root.children[index]
                if start:
                    path.append(char)
                    seen.add((i, j))
                    dfs(i, j, start)
                    seen.remove((i, j))
                    path.pop()
                
        return result 


        