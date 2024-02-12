class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:

        row_list = []  # результирующий список, содержащий отформатированные строки требуемой длины
        meter = 0  # счетчик слов в words
        row = []  # список(для получения одной строки) для формирорования очередной сроки для row_list
        meter_row = 0  # счетчик слов в одной формируемой строке row
        fill = 0  # счетчик заполненного места в очередной формируемой строке требуемой длины maxWidth
        row_list_last = ''  # переменная-string для последней строки

        while meter < len(words):
            # формирование в цикле по одной строке row из слов в words
            if len(words[meter]) <= maxWidth - fill:
                row.append(words[meter])
                fill += len(words[meter]) + 1
                meter += 1
                meter_row += 1
                if meter == len(words):  # если получается, что сформировалась последняя строка
                    row_list_last = " ".join(row).ljust(maxWidth)

            else:
                # начинаем форматирование очередной полученной строки
                delta = maxWidth - (
                            fill - meter_row)  # количество оставшихся, не заполненных в строке,необходимых распределить пробелов
                remain = 0  # количество пробелов, которые будем распределять неравномерно(начиная  слева) между словами в строке. Пока предполагаем, что 0
                if delta > 0:  # если сумма длины слов в одной строке (без одного пробела на слова) меньше    требуемой maxWidth,те. чтобы проверить, есть ли еще место
                    if meter_row > 1:  # число слов в строке больше одного
                        remain = delta % (meter_row - 1)
                        numbers_space_per_word = delta // (
                                    meter_row - 1) - 1  # вычисляем, сколько пробелов можно добавить РАВНОМЕРНО между словами(имея в виду, что еще один пробел между словами добавим присоединении списка в строку)
                    else:  # если всего одно слово в строке
                        remain = delta
                        numbers_space_per_word = delta
                        row = [row[0] + " " * remain]
                        remain = -1

                    if remain == 0:
                        row = [word + numbers_space_per_word * ' ' for word in row[:-1]] + [row[-1]]
                    elif remain > 0:  # слева пошагово добавляем пробелы в промежутки в строке, пока не закончатся пробелы (по факту, к словам справа)
                        i = 0
                        while remain > 0:
                            row[i] += ' '
                            i += 1
                            remain -= 1
                        row = [word + numbers_space_per_word * ' ' for word in row[:-1]] + [row[-1]]
                        ((numbers_space_per_word + 1) * " ").join(row)

                if remain == 0:
                    row_list.append(" ".join(row))
                elif remain == -1:
                    row_list.append("".join(row))
                row = []
                meter_row = 0
                fill = 0

        if row_list_last:
            row_list.append(row_list_last)

        return row_list


ex = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

for row in ex.fullJustify(words, maxWidth):
    print(row)

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
for row in ex.fullJustify(words, maxWidth):
    print(row)

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
for row in ex.fullJustify(words, maxWidth):
    print(row)