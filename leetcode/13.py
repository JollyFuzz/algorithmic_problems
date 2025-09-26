class Solution(object):
    def threeSum(self, raw_nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(raw_nums)

        result = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == -num:
                    result.append([num, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif curr_sum > -num:
                    right -= 1
                else:
                    left += 1
                    

        return result
    
# Solution().threeSum([-1,0,1,2,-1])
Solution().threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10])