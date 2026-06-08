class Solution:
    def intToRoman(self, num: int) -> str:
        # constantly subtract highest value
        # res string

        # If the value does not start with 4 or 9, select the symbol of the maximal value
        normal_mapping = [
            [1000, "M"],
            [500, "D"],
            [100, "C"],
            [50, "L"],
            [10, "X"],
            [5, "V"],
            [1, "I"],
        ]

        subtractive_mapping = [
            [900, "CM"],
            [400, "CD"],
            [90, "XC"],
            [40, "XL"],
            [9, "IX"],
            [4, "IV"],
        ]
        res = ""
        while num:
            if str(num)[0] in ["4", "9"]:
                for marker, chars in subtractive_mapping:
                    if num >= marker:
                        num -= marker
                        res += chars
                        break
            else:
                for marker, chars in normal_mapping:
                    if num >= marker:
                        num -= marker
                        res += chars
                        break
        return res

        