class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.pos = deque([[0,0]])
        self.food = deque(food)
        self.height = height
        self.width = width


    def move(self, direction: str) -> int:
        row, col = self.pos[0]

        if direction == "R":
            col += 1
        elif direction == "L":
            col -= 1
        elif direction == "U":
            row -= 1
        else:
            row += 1
        
        if min(row, col) < 0 or row == self.height or col == self.width:
            return -1
        
        # check food
        if self.food and [row, col] == self.food[0]:
            self.food.popleft()
        else:
            self.pos.pop()
        
        # check collision with self
        if [row, col] in self.pos:
            return -1
        
        self.pos.appendleft([row, col])
        return len(self.pos) - 1
        

        # check collision
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
