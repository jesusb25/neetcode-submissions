class Solution:
    def compress(self, chars: List[str]) -> int:
        start = 0
        stop = 0
        write = 0
        # everything after last write should be discarded

        while start != len(chars):
            while stop + 1 != len(chars) and chars[stop] == chars[stop + 1]:
                stop += 1
            
            length = stop - start + 1
            length_str = str(length)
            chars[write] = chars[start]
            write += 1
            if length != 1:
                for char in length_str:
                    chars[write] = char
                    write += 1
            start = stop = stop + 1

        while write != len(chars):
            chars.pop()
        return len(chars)
        




                    
