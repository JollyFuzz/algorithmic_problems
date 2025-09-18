# Дана последовательность числе длиной N
# Необходимо найти количество отрезков с нулевой суммой

#zsr - zero sum ranges 
def count_zsr(nums):
    """
    Можно посчитать префиксные суммы для каждого числа в последовательности
    Каждый раз когда мы натыкаемся сумму, которая уже была, значит мы получили отрезок с нулевой суммой
    4 1 2 -2 -1 5
    числа на отрезке от 1 до -1 "съели" себя
    """
    prefix_sum_by_value = {0: 1}

    cur_sum = 0
    for n in nums:
        cur_sum += n
        if cur_sum in prefix_sum_by_value:
            prefix_sum_by_value[cur_sum] += 1
        else:
            prefix_sum_by_value[cur_sum] = 1

    cnt_ranges = 0
    for cur_sum in prefix_sum_by_value.values():
        # Количество способов, которыми можно выбрать k элементов из n элементов (n choose k), определяется по формуле n! / (k! * (n - k)!)
        cnt_ranges += cur_sum * (cur_sum - 1) // 2

    return cnt_ranges

test_cases = [
    [[4, 1, 2, -2, -1, 5], 2]
]

print(count_zsr(test_cases[0][0]))