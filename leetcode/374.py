class Solution(object):
    def topKFrequent_v1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # получаем частотный словарь элементов
        # потом я бы его вывернула наизнанку и отсортировала частоту встречания
        # затем получила бы какие элементы встречаются чаще всего

        # получаем частотный словарь
        # n
        freq_nums = {}
        for n in nums:
            if n not in freq_nums:
                freq_nums[n] = 0
            freq_nums[n] += 1

        # вывораичваем частотный словарь наизнанку
        # n
        freq_values = {}
        for num, freq in freq_nums.items():
            if freq not in freq_values:
                freq_values[freq] = []
            freq_values[freq].append(num)

        # n*log(n)
        sorted_freq = sorted(freq_values)[::-1]
        result = []

        #n
        for freq in sorted_freq:
            result += freq_values[freq]
            if len(result) >= k:
                break

        return result[:k+1]
    
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # получаем частотный словарь элементов
        # потом я бы его вывернула наизнанку и отсортировала частоту встречания
        # затем получила бы какие элементы встречаются чаще всего

        # получаем частотный словарь
        # n
        freq_nums = {}

        for n in nums:
            if n not in freq_nums:
                freq_nums[n] = 0
            freq_nums[n] += 1

        # вывораичваем частотный словарь наизнанку
        # n
        freq_values = {}
        most_freq = 0
        for num, freq in freq_nums.items():
            if freq not in freq_values:
                freq_values[freq] = []
            freq_values[freq].append(num)
            if freq > most_freq:
                most_freq = freq

        result = []
        for freq in range(most_freq,0,-1):
            if freq in freq_values:
                result += freq_values[freq]

            if len(result) >= k:
                break

        return result[:k+1] 
            
Solution().topKFrequent([1,1,1,2,2,3], 2)