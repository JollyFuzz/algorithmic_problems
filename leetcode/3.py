# можно хранить те символы которые не нулевые
# дефаулт каунтер
def solution(s):
    # Иниализируем скользящее окно размером 1
    
    # Обходим строку, пока не дойдем до конца
    # Пока у нас все элементы в словаре счетчике по 1 пробуем увеличить размер окна
    # Если есть повторяющиеся элементы двигаем окно
    # При движении окна мы вычитаем в счетчике первую букву и добавляем новую
    # При расширении окна мы добавляем в счетчик букву

    # размер окна
    window_size = 1
    p = 0
    s_len = len(s)

    letter_conter = {s[0]: 1}

    while p < s_len - 1: # тут проверить границы
        # расширяем окно пока возможно
        while p+1 < s_len:
            p += 1
            letter = s[p]

            # если следующее число в подстроке повторяется, мы выходим из цикла расширения окна
            if letter_conter.get(letter, 0) != 0:
                break           
            
            letter_conter[letter] = letter_conter[letter] + 1 if letter in letter_conter else 1
            window_size += 1
            

        # скользим пока подстрока не станет уникальной
        while p < s_len:
            first_letter_i = p - window_size
            first_letter = s[first_letter_i]

            new_letter = s[p]

            letter_conter[first_letter] -= 1
            if new_letter not in letter_conter:
                letter_conter[new_letter] = 0
            letter_conter[new_letter] += 1

            if all(value < 2 for value in letter_conter.values()):
                break

            p += 1
            
    return window_size
    
cases = [
    "",
    "abcabcd",
    "aaaa",
    "abba",
    "ababab",
    "A",
    "AABC"
]
for c in cases:
    result = solution(c)
    print(f"{result} - {c}")