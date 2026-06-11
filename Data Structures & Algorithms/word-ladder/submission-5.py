class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Build pattern -> [words] map in O(N * L)
        patterns = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)

        # BFS -- find neighbors on-the-fly via patterns
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        print (patterns)

        while q:
            curr, changes = q.popleft()
            if curr == endWord:
                return changes

            for i in range(len(curr)):
                pattern = curr[:i] + "*" + curr[i+1:]
                for nei in patterns[pattern]:
                    if nei not in seen:
                        seen.add(nei)        # mark here, not on pop
                        q.append((nei, changes + 1))

        return 0