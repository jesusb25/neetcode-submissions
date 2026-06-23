class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.pos = deque([[0, 0]])
        self.width = width
        self.height = height
        self.food = deque(food)

    def move(self, direction: str) -> int:
        row, col = self.pos[0]
        if direction == "U":
            nr, nc = row - 1, col
        elif direction == "R":
            nr, nc = row, col + 1
        elif direction == "D":
            nr, nc = row + 1, col
        else:
            nr, nc = row, col - 1
        
        # check bounds
        if not (0 <= nr < self.height) or not 0 <= nc < self.width:
            return -1

        # eat food else pop tail  
        
        if not self.food or self.food[0] != [nr, nc]:
            self.pos.pop()
        else:
            self.food.popleft()

        if [nr, nc] in self.pos:
            return -1 
        self.pos.appendleft([nr, nc])
        
        

        return len(self.pos) - 1

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
