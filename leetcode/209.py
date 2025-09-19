#https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=prefix-sum
# Пробуем скользящим окном считать сумму, развигая его, пока не достигнем таргета
# как только достигли пробуем сдвинуть и сжать слева, получили новое наименьшее окно и потеряли таргет, повторяем


from typing import List


class Solution(object):
    # Решение через скользящее окно, но неоптимальная реализация скользящего
    def minSubArrayLen_v1(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        cur_summ = nums[0]
        best_min_subarr_len = None

        if len(nums) == 1 and nums[0] >= target:
            return 1
        
        while right < len(nums) - 1:
            # Расширяем скользящее окно пока не достигнем target
            while cur_summ < target and right + 1 < len(nums):
                right += 1
                cur_summ += nums[right]

            if cur_summ >= target and best_min_subarr_len is None:
                    best_min_subarr_len = right - left + 1   

            # скользим этим окном пока не получим снова сумму большую target
            while right + 1 < len(nums):
                cur_summ -= nums[left]
                left += 1
                right += 1
                cur_summ += nums[right]
                
                # останавливаемся когда дошли до нового отрезка, сумма которого больше таргета
                if cur_summ > target:
                    break
            
            # пробуем сжать окно слева
            while left < right: # проверить может ли left быть 0
                cur_summ -= nums[left]
                left += 1 

                # Прекращаем сжимать окно как только потеряли таргетную сумму
                if cur_summ < target:
                    break

                if best_min_subarr_len > right - left + 1:
                    best_min_subarr_len = right - left + 1

        return best_min_subarr_len if best_min_subarr_len is not None else 0

    def minSubArrayLen(self, target, nums):
        # левый указатель
        left = 0
        # Текущая сумма в скользящем окне
        cur_sum = 0

        best_len = len(nums) + 1
 
        # right - правый указатель
        for right in range(len(nums)):
            cur_sum += nums[right]

            if cur_sum >= target and best_len > right - left + 1:
                 best_len = right - left + 1

            while cur_sum >= target:
                cur_sum -= nums[left]
                left += 1
                
                if cur_sum >= target and best_len > right - left + 1:
                    best_len = right - left + 1

        return best_len if best_len <= len(nums) else 0
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0
# во всех циклах перепроврить точки выхода и выход за пределы массива

print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(Solution().minSubArrayLen(7, [8]))
print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))