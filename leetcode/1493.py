class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_zero = None
        left = None
        best_len = 0
        for right, n in enumerate(nums):
            if n == 0:
                if left is None:
                    continue

                if last_zero is not None:
                    left = last_zero + 1 if nums[last_zero+1] == 1 else None
                

                last_zero = None if left is None else right

            if n == 1:
                if left is None:
                    left = right

                new_sub_arr_len = right - left + 1 if last_zero is None else right - left
                if new_sub_arr_len > best_len:
                    best_len = new_sub_arr_len

        return best_len - 1 if best_len == len(nums) else best_len

