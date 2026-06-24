class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            char = chars[read]
            chars[write] = char
            write += 1
            scan = read
            while scan < len(chars) and char == chars[scan]:
                scan += 1
            
            length = int(scan - read)

            if length != 1:
                for char in str(length):
                    chars[write] = char
                    write += 1
            
                
            read = scan
        return write

