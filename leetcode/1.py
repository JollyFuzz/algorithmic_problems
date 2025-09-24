from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_pos_dict = {}
        for i, num in enumerate(nums):
            delta = target - num
            if delta in nums_pos_dict:
                return [i, nums_pos_dict[delta]]
            else:
                nums_pos_dict[num] = i

Solution().twoSum([2,7,11,15], 9)