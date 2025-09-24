class Solution:
    #неоптимальное решение, сложное и неучтен вариант если заменять крайние k 
    def characterReplacement_v1(self, s: str, k: int) -> int:
        # Считаем промежутки
        characters_ranges = {}
        curr_char = None
        curr_range_start = None
        curr_range_end = None
        for i, c in enumerate(s):
            # если мы встретили новый символ, не продолжающий предыдущую последовательность
            # то мы завершаем подсчет текущего отрезка для этого символа
            if c != curr_char:
                # None у нас только в самом начале
                if curr_char is not None:
                    # Заводим список для символа, если его еще не существует
                    if not curr_char in characters_ranges:
                        characters_ranges[curr_char] = []
                    #
                    characters_ranges[curr_char].append((curr_range_start, curr_range_end))
                
                # Инициализируем переменные для нового диапазона
                curr_char = c
                curr_range_start = i
                curr_range_end = i
                
            else:
                # продожаем считать для этого диапазона символа
                curr_range_end += 1
        else:
            if not curr_char in characters_ranges:
                    characters_ranges[curr_char] = []
                
            characters_ranges[curr_char].append((curr_range_start, curr_range_end))

        for c, ranges in characters_ranges.items():
            left = 0
            rest_k = k
            best_len = 0
            curr_len = 0
            for right, c_range in enumerate(ranges):
                curr_len += c_range[1] - c_range[0] + 1
                if right - 1 >= 0:
                    prev_c_range = ranges[right - 1]
                    rest_k -= c_range[0] - prev_c_range[1] - 1

                while rest_k < 0 and left < right:
                    last_range = ranges[left]
                    next_left_range = ranges[left + 1]
                    curr_len -= (last_range[1] - last_range[0] + 1)
                    rest_k += (next_left_range[0] - last_range[1] - 1)
                    left += 1

                if k >= 0 and curr_len + (k - rest_k) > best_len:
                    best_len = curr_len + k - rest_k

            return best_len
                
    def characterReplacement(self, s: str, k: int) -> int:
        chars_frequency = {}
        max_freq = 0
        left = 0
        for right, c in enumerate(s):
            # инициализируем символ в хеш таблице если его нет
            if not c in chars_frequency:
                chars_frequency[c] = 0
            
            chars_frequency[c] += 1

            # получаем количество самого частотного символа
            if chars_frequency[c] > max_freq:
                max_freq = chars_frequency[c]

            

            
            

# print(Solution().characterReplacement("ABABBAAABA", 2))
print(Solution().characterReplacement("ABAB", 2))
# print(Solution().characterReplacement("A", 2))
# что с одним символом