class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # Queue stores (i, j, ops_so_far)
        q = deque()
        q.append((0, 0, 0))
        visited = set()
        visited.add((0, 0))

        while q:
            i, j, ops = q.popleft()

            # If we've finished processing both strings
            if i == m and j == n:
                return ops

            # Option 1: Characters match – advance both with no extra cost
            if i < m and j < n and word1[i] == word2[j]:
                if (i + 1, j + 1) not in visited:
                    visited.add((i + 1, j + 1))
                    q.appendleft((i + 1, j + 1, ops))  # 0-weight edge – push to front
            else:
                # Option 2: Insert word2[j] into word1 (move j forward)
                if j < n and (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    q.append((i, j + 1, ops + 1))

                # Option 3: Delete word1[i] (move i forward)
                if i < m and (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    q.append((i + 1, j, ops + 1))

                # Option 4: Replace word1[i] with word2[j] (move both forward)
                if i < m and j < n and (i + 1, j + 1) not in visited:
                    visited.add((i + 1, j + 1))
                    q.append((i + 1, j + 1, ops + 1))

        return 0  # fallback (should never be reached)
