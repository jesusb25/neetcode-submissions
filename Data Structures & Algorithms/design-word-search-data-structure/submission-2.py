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
        
        def dfs(node, target):
            if target == "":
                return node.end

            
            if target[0] == ".":
                options = node.children
            else:
                i = ord(target[0]) - ord('a')
                options = [node.children[i]]
            
            for option in options:
                if not option:
                    continue
                if dfs(option, target[1:]): return True
            return False
            
            

        return dfs(self.root, word)

        
