def solution(a):
    left_p = 0
    right_p = len(a) - 1

    left_v = a[left_p] ** 2
    right_v = a[right_p] ** 2

    result_a = []

    while left_p <= right_p:
        if left_v > right_v:
            result_a.insert(0, left_v)

            left_p += 1
            left_v = a[left_p] ** 2
        else:
            result_a.insert(0, right_v)

            right_p -= 1
            right_v = a[right_p] ** 2


    return result_a
        

# самый оптимальный вариант=)
def solution1(a):
    result = []
    for num in a:
        result.append(num ** 2)
    return sorted(result)

            
# Хороший вариант, тоже оптимальный, вот так стоит улучшить мое решение
def solution2(nums):
    n = len(nums)
    l, r = 0, n - 1
    res = [0] * n
    last = n - 1

    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res[last] = nums[l]**2
            l += 1
        else:
            res[last] = nums[r]**2
            r -= 1
        last -= 1
    return res




if __name__ == "__main__":
    cases = [
        [-4,-1,0,3,10],
        [-3,-2,-1],
        [-3,-2,-1,0],
        [1,2,3],
        [0,1,2,3],
        [-2,-1,0,1,2]
    ]
    for c in cases:
        r = solution(c)
        expected_c = sorted([i ** 2 for i in c])
        print(f"{r == expected_c} - { c } - { r } ")