from typing import List


class Solution:
    # неправильный подход, учтена ситуация только для положительных чисел 
    def subarraySum_v1(self, nums: List[int], k: int) -> int:
        left = 0
        total = 0

        count = 0
        for right in range(len(nums)):
            total += nums[right]

            while (k > 0 and total > k or k < 0 and total < k or k == 0 and total != k) and left < right:
                total -= nums[left]
                left += 1

            if total == k:
                count += 1

        
        return count
    
    
    def subarraySum_v2(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}

        total_sum = 0
        count = 0
        get_remainder = self.get_remainder(k)
        for i, num in enumerate(nums):
            total_sum += num

            if num == k:
                count += 1

            remainder = get_remainder(total_sum, k)
            if remainder in prefix_sum:
                count += prefix_sum[remainder]

            if not total_sum in prefix_sum:
                prefix_sum[total_sum] = 0

            prefix_sum[total_sum] += 1



        return count
    
    def subarraySum_v3(self, nums: List[int], k: int) -> int:
        # Словарь для хранения частот встречающихся префиксных сумм
        prefix_sum_count = {0: 1}  # Начальное значение: нулевая сумма встречается ровно 1 раз
        
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            
            # Вычисляем разницу между текущей суммой и целевой суммой k
            diff = current_sum - k
            
            # Если разница уже была ранее, значит нашли подходящие подмассивы
            if diff in prefix_sum_count:
                result += prefix_sum_count[diff]
                
            # Обновляем частоту текущей суммы
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1
        
        return result

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0: 1}

        total_sum = 0
        count = 0
        for num in nums:
            total_sum += num

            diff = total_sum - k

            count += prefix_sum_count.get(diff, 0)

            if not total_sum in prefix_sum_count:
                prefix_sum_count[total_sum] = 0

            prefix_sum_count[total_sum] += 1
        
        return count

            



        

assert Solution().subarraySum([1,1,1], 2)  == 2
assert Solution().subarraySum([-1,-1,1], 1) == 1
assert Solution().subarraySum([-1,-1,1], 0) == 1