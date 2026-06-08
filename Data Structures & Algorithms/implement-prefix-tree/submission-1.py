class TrieNode:

    def __init__(self, val = None, end = False):
        self.val = val
        self.end = False
        self.next = {} # char to next node


class PrefixTree:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.next:
                curr.next[char] = TrieNode(char)
            
            curr = curr.next[char]
        
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            if char not in curr.next:
                return False
            
            curr = curr.next[char]
        
        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            if char not in curr.next:
                return False
            
            curr = curr.next[char]
        
        return True
        
        
        