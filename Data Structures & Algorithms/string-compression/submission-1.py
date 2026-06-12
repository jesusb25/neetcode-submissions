class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = read = 0

        while read < n:
            # read and write group char
            group_char = chars[read]
            chars[write] = group_char
            write += 1

            # scan consecutive
            scan = read
            while scan < n and chars[scan] == group_char:
                scan += 1
            
            # get length
            length = scan - read
            if length != 1:
                for char in str(length):
                    chars[write] = char
                    write += 1
            read = scan
        return write


