terms = '''
Given a positive integer n, find and return the longest distance 
between any two adjacent 1's in the binary representation of n. 
If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). 
The distance between two 1's is the absolute difference between their bit positions. 
For example, the two 1's in "1001" have a distance of 3.
'''


class Solution:
    def binaryGap(self, n: int) -> int:

        if n < 3:
            return 0

        n_bytes = bin(n)[2:]

        if n_bytes.count('1') < 2:
            return 0

        last = longest_distance = 0

        for i, e in enumerate(n_bytes):
            if e == '1':
                distance = i - last
                if distance > longest_distance:
                    longest_distance = distance
                last = i

        return longest_distance


if __name__ == '__main__':

    sol = Solution()

    s = sol.binaryGap(22)
    print(s)
    s = sol.binaryGap(8)
    print(s)
    s = sol.binaryGap(5)
    print(s)
    s = sol.binaryGap(3)
    print(s)
    s = sol.binaryGap(13)
    print(s)
