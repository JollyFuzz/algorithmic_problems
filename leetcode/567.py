class Solution:
    @staticmethod
    def count_symbols(s):
        symbols_table = {}
        for symbol in s:
            if symbol not in symbols_table:
                symbols_table[symbol] = 0
            symbols_table[symbol] += 1

        return symbols_table

    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_symbols_dict = self.count_symbols(s1)
        slide_win_symbols = self.count_symbols(s2[:len(s1)])

        if slide_win_symbols == target_symbols_dict:
            return True

        for left in range(1, len(s2) - len(s1) + 1):
            right = left + len(s1) - 1

            slide_win_symbols[s2[left - 1]] -= 1
            if slide_win_symbols[s2[left - 1]] == 0:
                del slide_win_symbols[s2[left - 1]]

            if not s2[right] in slide_win_symbols:
                slide_win_symbols[s2[right]] = 0
            slide_win_symbols[s2[right]] += 1

            if slide_win_symbols == target_symbols_dict:
                return True
        
        return False
    
Solution().checkInclusion("adc", "dcda")
        