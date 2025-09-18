
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Поместим указатели на первый и на последний элемент
        # Вычислять площадь будем по min(hp1, hp2)*(p2-p1)
        # Смещаем указатель на более низкой линии дальше
        left = 0
        right = len(height) - 1
        max_V = 0

        while left < right:
            new_V = min(height[left], height[right])*(right - left)
            if new_V > max_V:
                max_V = new_V

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_V

test_case = [1,8,6,2,5,4,8,3,7]
result = Solution().maxArea(test_case)
print(result)