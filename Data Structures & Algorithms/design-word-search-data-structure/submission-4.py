class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        
        curr.end = True
        

    def search(self, word: str) -> bool:
        
        def dfs(node, index):
            if index == len(word):
                return node.end
            
            if word[index] == ".":
                options = node.children
            else:
                options = [node.children[ord(word[index]) - ord('a')]]
            
            for option in options:
                if option and dfs(option, index + 1):
                    return True
            return False
            
            

        return dfs(self.root, 0)

        
