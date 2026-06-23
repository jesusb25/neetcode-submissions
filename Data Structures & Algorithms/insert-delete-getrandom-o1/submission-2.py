class RandomizedSet:

    def __init__(self):
        self.stack = []
        self.indices = {}
        

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.indices[val] = len(self.stack)
        self.stack.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        curr_i = self.indices[val]
        tail = self.stack.pop()
        del self.indices[val]
        if curr_i != len(self.stack):
            self.stack[curr_i] = tail
            self.indices[tail] = curr_i
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.stack)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()