from typing import List

# 22min
# https://leetcode.com/problems/merge-sorted-array/
class Solution:

    def shift_right(self, nums, pos):
        for i in range(len(nums)-1,pos,-1):
            nums[i] = nums[i-1]

        return


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                self.shift_right(nums1, p1)
                nums1[p1] = nums2[p2]
                p1 += 1
                p2 += 1
                m += 1

        for i in range(p2,n):
            nums1[p1] = nums2[i]
            p1 += 1

        return
        
                
    

print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(Solution().merge([1], 1, [], 0))
        