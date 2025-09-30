class Solution(object):
    # def maximumCount(self, nums):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     # Возможно нам ничего не нужно искать и у нас простой случай:
    #     # Массив полностью состоит из отрицательных или положительных чисел
    #     if nums[0] < 0 and nums[-1] < 0 or nums[0] > 0 and nums[-1] > 0:
    #         return len(nums)
        
    #     # массив полностью состоит из нулей 
    #     if nums[0] == nums[-1] == 0:
    #         return 0
        
    #     start = 0
    #     end = len(nums) - 1

    #     neg_bound = 0
       
    #    # Если в массиве есть отрицательные числа, то мы ищем границу отрицательных числе
    #     if nums[0] < 0:
    #         while start <= end:
    #             middle_i = start + (end - start) // 2
                
    #             if nums[middle_i] < 0 and nums[middle_i+1] >= 0:
    #                 neg_bound = middle_i
    #                 break

    #             if nums[middle_i] >= 0:
    #                 end = middle_i - 1
    #             else:
    #                 start = middle_i + 1
                    
    #         # если у нас в массиве нет нулей, то мы можем сразу посчитать каких чисел больше 
    #         if nums[neg_bound+1] != 0:
    #             return max(neg_bound + 1, len(nums) - neg_bound - 1)
            
    #         # или если отрицательных чисел больше половины, то в любом случае положительных буде меньше и можем завершать работу
    #         if neg_bound + 1 > len(nums) // 2 or nums[-1] == 0:
    #             return neg_bound + 1
            
    #     # Ищем границу положительных чисел
    #     pos_bound = None
    #     start = neg_bound + 1
    #     end = len(nums) - 1
    #     while start <= end:
    #         middle_i = start + (end - start) // 2

    #         if nums[middle_i] != 0 and nums[middle_i-1] == 0:
    #             pos_bound = middle_i
    #             break

    #         if nums[middle_i] == 0:
    #             start = middle_i + 1
    #         else:
    #             end = middle_i - 1

    #     return max(len(nums)-pos_bound, neg_bound+1)

    def maximumCount(self, nums):
        # Возможно нам ничего не нужно искать и у нас простой случай:
        # Массив полностью состоит из отрицательных или положительных чисел
        if nums[0] < 0 and nums[-1] < 0 or nums[0] > 0 and nums[-1] > 0:
            return len(nums)
        
        # массив полностью состоит из нулей 
        if nums[0] == nums[-1] == 0:
            return 0
        

print(Solution().maximumCount([-2,-1,-1,1,2,3]))
# print(Solution().maximumCount([-3,-2,-1,0,0,1,2]))
# print(Solution().maximumCount([5,20,66,1314]))