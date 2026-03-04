'''Convert roman numberals without converting to string'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tally = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s):
                current = s[i]
                next = s[i + 1]

                if current == "I" and next == "V":
                    tally += 4
                    i += 2
                    continue
                elif current == "I" and next == "X":
                    tally += 9
                    i += 2
                    continue
                elif current == "X" and next == "L":
                    tally += 40
                    i += 2
                    continue
                elif current == "X" and next == "C":
                    tally += 90
                    i += 2
                    continue
                elif current == "C" and next == "D":
                    tally += 400
                    i += 2
                    continue
                elif current == "C" and next == "M":
                    tally += 900
                    i += 2
                    continue

            tally += roman_dict[s[i]]
            i += 1

        return tally

my_solution = Solution()
print(my_solution.romanToInt("III"))
print(my_solution.romanToInt("LVIII"))
print(my_solution.romanToInt("MCMXCIV"))
