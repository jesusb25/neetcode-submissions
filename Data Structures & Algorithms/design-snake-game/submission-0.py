class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.pos = deque([[0, 0]])
        self.score = 0
        self.q = deque(food)
        self.width = width
        self.height = height

    def move(self, direction: str) -> int:
        r, c = self.pos[0]
        
        if direction == "R":
            c += 1
        elif direction == "D":
            r += 1
        elif direction == "U":
            r -= 1
        else:
            c -= 1
        
        # check bounds
        if r < 0 or r == self.height or c < 0 or c == self.width:
            return -1

        # check food
        if self.q and [r, c] == self.q[0]:
            self.q.popleft()
            self.score += 1
        else:
            self.pos.pop()
            # check collision with body
            if [r, c] in self.pos:
                return -1
        
        self.pos.appendleft([r, c])
        return self.score