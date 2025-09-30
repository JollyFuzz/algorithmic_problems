class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # получаем для каждого y - площадь и общую площадь
        prefix_sum_y = {}
        max_y = 0
        for x, y, l in squares:
            for i in range(y+1, y+l+1):
                if i not in prefix_sum_y:
                    prefix_sum_y[i] = 0
                
                prefix_sum_y[i] += l 

                if i > max_y:
                    max_y = i

        squares_sum = sum(prefix_sum_y.values())
        half_squares = squares_sum / 2

        curr_sum = 0
        i = 0

        while curr_sum < half_squares:
            i += 1
            if i in prefix_sum_y:
                curr_sum += prefix_sum_y[i]

        bottom_square  = curr_sum - prefix_sum_y[i]
        top_square = squares_sum - curr_sum
        middle_square = prefix_sum_y[i]

        target_y = (top_square - bottom_square + middle_square) / (2*middle_square)

        return i - 1 + target_y


        # затем бинарным поиском ищем гдле у нас половина суммы


tc = [[0,0,1],[2,2,1]]
tc = [[0,0,2],[1,1,1]]
tc = [[23,29,3],[28,29,4]]
print(Solution().separateSquares(tc))