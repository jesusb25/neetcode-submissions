class RandomizedSet:

    def __init__(self):
        self.vals = {} # val to index
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.vals[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False

        # replace with last value and pop
        if self.vals[val] != len(self.arr) - 1:
            val_i = self.vals[val]
            self.arr[val_i] = self.arr[-1]
            self.vals[self.arr[val_i]] = val_i

        del self.vals[val]
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()