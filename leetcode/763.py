class Solution(object):
    def partitionLabels_v1(self, s):
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
    
    def partitionLabels_v2(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # Составляем словарь символ: последнее значение
        # Обходим строку еще раз, для каждого символа смотрим, когда он встречается в строке последний раз
        # если последнее вхождение символа правее указателя end для отрезка, то мы меняем указатель end на позицию вхождения последнего символа
        # если мы дошли указателя end, то можем обрезать строку
        last_symbols_pos = {symb: i for i, symb in enumerate(s)}
        end = 0
        labels = []

        labels_len = 0

        for i, symb in enumerate(s):
            last_symb_pos = last_symbols_pos[symb]

            if last_symb_pos > end:
                end = last_symb_pos

            if i == end:
                substr_len = i - labels_len + 1
                labels_len += substr_len
                labels.append(substr_len)
        
        return labels
    
    def partitionLabels(self, s):
        """
        Разделяем строку на непересекающиеся метки,
        где каждая буква в пределах одной метки повторяется только в рамках самой метки.
        Возвращается список длин меток.
        """
        # Создаем словарь, где ключ - символ, значение - последняя позиция этого символа в строке
        last_occurrence = {ch: idx for idx, ch in enumerate(s)}

        start = 0   # Начало текущей метки
        end = 0     # Конец текущей метки
        partitions = []  # Список длин меток

        for i, char in enumerate(s):
            # Получаем последнюю позицию текущего символа
            last_position = last_occurrence[char]
            
            # Если последняя позиция больше текущего конца метки, сдвигаем конец вправо
            if last_position > end:
                end = last_position
                
            # Если достигли конца текущей метки, добавляем её длину в результат
            if i == end:
                length = end - start + 1
                partitions.append(length)
                start = i + 1  # Начинаем новую метку с следующей позиции

        return partitions



Solution().partitionLabels("ababcbacadefegdehijhklij")
# Solution().partitionLabels("eccbbbbdec")



