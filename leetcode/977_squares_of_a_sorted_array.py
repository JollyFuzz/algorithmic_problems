# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# 9:55
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares_nums = [0] * len(nums)
        squares_p = len(squares_nums) - 1

        left_p = 0
        right_p = len(nums) - 1

        while left_p <= right_p:
            if abs(nums[left_p]) > abs(nums[right_p]):
                squares_nums[squares_p] = nums[left_p] ** 2
                left_p += 1
            else:
                squares_nums[squares_p] = nums[right_p] ** 2
                right_p -= 1

            squares_p -= 1

        return squares_nums
    
Solution().sortedSquares([-7,-3,2,3,11]) 
        