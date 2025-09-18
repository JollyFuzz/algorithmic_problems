# https://leetcode.com/problems/sum-of-variable-length-subarrays/description/
class Solution(object):
    # это решение с префиксными суммами
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Построить массив префиксных сумм для массива
        # Для каждого числа по заданному условию определить сумму

        # построение префиксной суммы
        prefix_sum = []
        for i, n in enumerate(nums):
            if i == 0:
                prefix_sum.append(n)
            else:
                prefix_sum.append(prefix_sum[-1] + n)
        
        result_sum = 0
        for i, n in enumerate(nums):
            start = max(0, i - n)
            # Прибавляем nums[start] т.к. теряем его при вычитании
            result_sum += prefix_sum[i] - prefix_sum[start] + nums[start] if i != start else n
        
        return result_sum

nums = [2,3,1]
print(Solution().subarraySum(nums))