class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            group_char = chars[read]
            chars[write] = group_char
            write += 1
            start = read
            while read < len(chars) and chars[read] == group_char:
                read += 1
            
            length = read - start

            if length != 1: 
                length_str = str(length)
                for i in range(len(length_str)):
                    chars[write] = length_str[i]
                    write += 1

        return write


            
