from typing import List

TARGET_LEN = 4

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        four_sums = {}
        for i1, n1 in enumerate(sorted_nums):
            for i2 in range(i1+1, len(nums)):
                n2 = sorted_nums[i2]
                for i3 in range(i2+1, len(nums)):
                    n3 =  sorted_nums[i3]
                    for i4 in range(i3+1, len(nums)):
                        n4 =  sorted_nums[i4]
                        curr_summ = n1 + n2 + n3 + n4
                        if curr_summ == target and (n1,n2,n3,n4) not in four_sums:
                            four_sums[(n1, n2, n3, n4)] = None
                        
                        if curr_summ > target:
                            break
        
        return list(four_sums.keys())
Solution().fourSum([2,2,2,2,2], 8)
