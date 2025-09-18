class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # !!!!это не оптмиальное решение + здесь недореализован подсчет длины отрезка

        # считаем буквы в частях при помощи хеш таблиц
        # ставим указатель на первую букву
        # как толоко мы встречаем новую букву указателем, пробуем разделить строку
        # при этом если найденная буква встречалась в хеш таблице более ранних частей, то объединяем эти части

        # список хеш-таблиц отрезков

        partitions = []
        for symbol_index, symbol in enumerate(s):
            merge_num = None

            # ищем символ в предыдущих отрезках 
            for part_num, part in enumerate(partitions):
                if symbol in part:
                    merge_num = part_num 
                    break
            
            # если нашли, то начиаем объединять хеш-таблицы
            if merge_num is not None:
                # вот тут не реализован случай если символ найден в последнем отрезке
                while len(partitions) > merge_num+1:
                    cur_part = partitions.pop(-1)
                    last_part = partitions[-1]
                    l = cur_part["len"] + last_part["len"] + 1 # и тут кажется проблема с подсчетом отрезка
                    partitions[-1] = {**last_part, **cur_part}
                    partitions[-1]["len"] = l
            else:
                partitions.append({symbol: None, "len": 1})

        return partitions
    


Solution().partitionLabels("ababcbacadefegdehijhklij")
# Solution().partitionLabels("eccbbbbdec")



