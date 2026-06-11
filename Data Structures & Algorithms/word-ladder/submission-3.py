class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # adj list using neighoring words
        adj = defaultdict(set) # word; neighbors
        def checkNei(word1, word2):
            diffs = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diffs += 1
                
                if diffs > 1:
                    return False
            return diffs == 1

        for word in wordList + [beginWord]:
            for nei in wordList + [beginWord]:
                if checkNei(word, nei) and word != nei:
                    adj[nei].add(word)
                    adj[word].add(nei)

        
        q = deque([[beginWord, 1]])
        seen = set()
        while q:
            curr, changes = q.popleft()
            if curr == endWord:
                return changes

            seen.add(curr)
            for nei in adj[curr]:
                if nei not in seen:
                    q.append([nei, changes + 1])




        return 0



