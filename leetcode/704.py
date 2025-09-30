class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            middle_i = start + (end - start) // 2
            middle_num = nums[middle_i]
            
            if middle_num == target:
                return middle_i
                
            elif target < middle_num:
                end = middle_i - 1
            else:
                start = middle_i + 1
        
        return -1


print(Solution().search(list(range(1,8)), 6))