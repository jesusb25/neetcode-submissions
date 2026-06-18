class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        
        count = Counter(words[0])

        res = []

        for word in words:
            cur_count = Counter(word)

            for key in count:
                if key not in cur_count:
                    count[key] = 0

                count[key] = min(count[key], cur_count[key])
            
        for key in count:
            for i in range(count[key]):
                res.append(key)
        return res