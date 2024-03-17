class Solution:
    # 1 <= s.length <= 15
    # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    # It is guaranteed that s is a valid roman numeral in the range [1, 3999].
    def romanToInt(self, s: str) -> int:


        # I can be placed before V (5) and X (10) to make 4 and 9.
        # X can be placed before L (50) and C (100) to make 40 and 90.
        # C can be placed before D (500) and M (1000) to make 400 and 900.
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        roman_ranks = {
            0: 'M',
            1: 'D',
            2: 'C',
            3: 'L',
            4: 'X',
            5: 'V',
            6: 'I'
        }

        s = s.upper()

        for roman in roman_ranks.items():
            roman_rank = roman[0]
            roman_number = roman[1]
            # print(roman_number)
            # print(s.find(roman_number))

            # TODO complete dat task
            while s.find(roman_number) != -1:
                current_index = s.find(roman_number)
                print(current_index)

                if current_index != 0:
                    # print(s[1])
                    # print(s[0])
                    prev_roman = s[current_index - 1]
                    print(prev_roman)


        return 1


if __name__ == '__main__':
    Solution().romanToInt('MM')