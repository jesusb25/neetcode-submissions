class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # --- BFS from Pacific (top and left edges) ---
        pacific = set()
        q = deque()

        # Top row
        for c in range(COLS):
            q.append((0, c, heights[0][c]))
            pacific.add((0, c))
        # Left column (skip (0,0) already added, but set handles duplicates)
        for r in range(1, ROWS):
            q.append((r, 0, heights[r][0]))
            pacific.add((r, 0))

        while q:
            r, c, h = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in pacific:
                    if heights[nr][nc] < h:   # can't flow upward from ocean
                        continue
                    pacific.add((nr, nc))
                    q.append((nr, nc, heights[nr][nc]))

        # --- BFS from Atlantic (bottom and right edges) ---
        atlantic = set()
        q = deque()

        # Bottom row
        for c in range(COLS):
            q.append((ROWS - 1, c, heights[ROWS - 1][c]))
            atlantic.add((ROWS - 1, c))
        # Right column (skip bottom-right corner already added)
        for r in range(ROWS - 1):
            q.append((r, COLS - 1, heights[r][COLS - 1]))
            atlantic.add((r, COLS - 1))

        while q:
            r, c, h = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in atlantic:
                    if heights[nr][nc] < h:
                        continue
                    atlantic.add((nr, nc))
                    q.append((nr, nc, heights[nr][nc]))

        # --- Intersection: cells reachable from both oceans ---
        return [[r, c] for r in range(ROWS) for c in range(COLS) 
                if (r, c) in pacific and (r, c) in atlantic]