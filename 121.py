"""
Задача: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""
class Solution(object):
    # сложное и неоптимальнрое решение
    def maxProfitv1(self, nums):
        """
        # Ищем минимальное и максимальное число в последовательности и их индексы
        # Если их несколько берем крайнее левое наименьшее и крайнее правое наибольшее
        
        # Если min левее max, то мы нашли решение
        # В противном случае ищем наименьшее число левее макисмальное и наибольшее правее минимального
        # Наибольшая дельта для найденных пар и будет решением
        """
        if len(nums) == 0:
            return 0
        
        min_num = nums[0]
        min_num_pos = 0

        max_num = nums[0]
        max_num_pos = 0

        # Ищем минимальное и максимальное число в последовательности и их индексы
        for i, num in enumerate(nums):
            # Равенство нестрогое, т.к. нам нужно первое минимальное
            if min_num > num:
                min_num = num
                min_num_pos = i
            
            # Равенство строгое, т.к. нам нужно последнее максимальное
            if max_num <= num:
                max_num = num
                max_num_pos = i

        if max_num_pos == min_num_pos:
            # Элементы одинаковые, нет решения
            return 0
        elif max_num_pos > min_num_pos:
            return max_num - min_num
        elif max_num_pos == 0 and min_num_pos == len(nums) -1:
            return self.maxProfit(nums[1:-1])
        elif max_num_pos == 0:
            return self.maxProfit(nums[1:])
        elif min_num_pos == len(nums) -1:
            return self.maxProfit(nums[:-1])
        
        # Максимальное число в последовательности левее минимального, 
        # поэтому для найденных максимального и минимального числа ищем пары\
        left_min_num = min(nums[:max_num_pos+1])
        right_max_num = max(nums[min_num_pos:])

        return max(max_num - left_min_num, right_max_num - min_num)
    
    # сложное и неоптимальнрое решение
    def maxProfitV2(self, nums):
        """
        # Ищем минимальное и максимальное число в последовательности и их индексы
        # Если их несколько берем крайнее левое наименьшее и крайнее правое наибольшее
        
        # Если min левее max, то мы нашли решение
        # В противном случае ищем наименьшее число левее макисмальное и наибольшее правее минимального
        # Наибольшая дельта для найденных пар и будет решением
        """
        min_num_pos = 0
        max_num_pos = 0
        while True:
            if len(nums) < 2:
                return 0
            
            min_num = nums[0]
            min_num_pos = 0

            max_num = nums[0]
            max_num_pos = 0
            # Ищем минимальное и максимальное число в последовательности и их индексы
            for i, num in enumerate(nums):
                # Равенство нестрогое, т.к. нам нужно первое минимальное
                if min_num > num:
                    min_num = num
                    min_num_pos = i
                
                # Равенство строгое, т.к. нам нужно последнее максимальное
                if max_num <= num:
                    max_num = num
                    max_num_pos = i

            if max_num_pos == min_num_pos:
                # Элементы одинаковые, нет решения
                return 0
            elif max_num_pos > min_num_pos:
                return max_num - min_num
            elif max_num_pos == 0 and min_num_pos == len(nums) -1:
                nums = nums[1:-1]
            elif max_num_pos == 0:
                nums = nums[1:]
            elif min_num_pos == len(nums) -1:
                nums = nums[:-1]
            else:
                break
        
        # Максимальное число в последовательности левее минимального, 
        # поэтому для найденных максимального и минимального числа ищем пары\
        left_min_num = min(nums[:max_num_pos+1])
        right_max_num = max(nums[min_num_pos:])

        return max(max_num - left_min_num, right_max_num - min_num)

    def maxProfit(self, nums):
        """
        Вводим переменные, хранящие локальные минимумы и максимумы
        Будем искать локальный минимум и локальный максимум правее него, такие что разница между ними будет наибольшая
        В начальный момент времени локлаьный минимум равен первому элементу, а локального максимума нет.
        Как только мы встречаем число большее локального минимума, то назначаем его локальным максимумом и высчитываем разница между ними

        Двигаемся по строке и обновляем значения переменных при следующий условиях:
        1. Число меньше, чем локальный минимум => оно становится локальным минимумом, локальный максимум затирается(и мы еще его снова по логике выше)
        2. Число больше чем локальный максимум => оно становится локальным максимумом
        3. При обновлении локального минимума и локального максимума высчитывается новый профит, если он лучше предыдщего, то сохраняем его как наилучший 
        """
        local_min = nums[0]
        local_max = None

        best_profit = 0

        for num in nums:
            if num < local_min:
                local_min = num
                local_max = None

            if not local_max or num > local_max:
                local_max = num
                profit = local_max - local_min
                if profit > best_profit:
                    best_profit = profit

        return best_profit


# Тестовые случаи
test_cases = [
    [[7,1,5,3,6,4], 5], # стандарный
    [[7,6,4,3,1], 0], # нет решения
    [[1, 1, 1], 0],
    [[1], 0],
    [[3,4,1,7,6], 6],
    [[3,4,7,1,6], 5],
    [[4, 5, 1, 6, 7, 3, 1], 6],
    [[7,2,4,1], 2],
    [[7, 1], 0],
    [[11,2,7,1,4], 5],
    [[2,4,1], 2],
    [[10, 11, 2, 7, 1, 4], 5]


]

for case, answer in test_cases:
    solver = Solution()
    result = solver.maxProfit(case)
    print(f"{result == answer} - {result} - {answer}")