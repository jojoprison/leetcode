from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        total = 0

        while nums:
            total += int(f'{nums.pop(0)}{nums.pop()}') if len(nums) > 1 else nums.pop()

        return total


if __name__ == '__main__':
    sol = Solution()

    s1 = sol.findTheArrayConcVal([7, 52, 2, 4])
    print(s1)
    s2 = sol.findTheArrayConcVal([5, 14, 13, 8, 12])
    print(s2)
