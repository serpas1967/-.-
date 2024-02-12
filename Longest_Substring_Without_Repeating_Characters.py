class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind = 0
        substr = ''
        max_len = 0
        dict_substr = dict()
        dict_substr[0] = 0

        while ind < len(s):  # проходим строку s по-символьно
            if s[ind] not in substr:  # если очередной символ из строки s отсутствует в подстроке искомой substr, то
                                      # добавляем его в в подстроку substr
                substr += s[ind]
            else:
                ind = s.find(s[ind], ind - len(substr)) + 1  # если очередной символ из строки s уже      #присутствует в текущей подстроке substr, то нужно искать ЗАНОВО нужную подстроку substr, НАЧИНАЯ с #элемента, который следует в s после символа, у которого нашелся дубль в s
                substr = s[ind]
            if len(substr) > max_len:
                dict_substr[substr] = len(substr)
                max_len = len(substr)
            ind += 1

        substr = max(dict_substr, key=dict_substr.get)

        return f"Длина максимальной подстроки {substr} без повторяющихся символов! в строке {s}  равна  {max_len}"




s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))