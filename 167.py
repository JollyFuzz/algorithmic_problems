class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0 
        right = len(numbers) - 1
        while left < right:
            val_left = numbers[left]
            val_right = numbers[right]

            if val_left + val_right == target:
                return [left+1, right+1]
            
            if target - val_left < val_right:
                right -= 1
                continue

            if target - val_right > val_left:
                left += 1
                continue
        
        return []
