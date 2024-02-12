class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        result = []
        len_word = len(words[0])  # длина каждого слова в words
        len_substr = len(words) * len_word  # длина всех слов в  words
        len_s = len(s)  # длина стороки s
        start = 0
        # words_dict = {word: words.count(word) for word in words}  через словарь не проходит/не принимает по времени
        words_list_sort = sorted(words)  # отсортированный список words
        while start + len_substr <= len_s:
            window = s[start: start + len_substr]  # формируем "окно" длиной равное сумме длин слов в words

            # разбиваем "окно, равное по длине набору слов из words" на слова, каждое длиной одно слово в words , формируем список и сортируем его
            window_list_sort = sorted([window[ind: ind + len_word] for ind in range(0, len(window), len_word)])
            # window_dict = {el: window_list.count(el) for el in window_list}   через словарь не проходит/не принимает по времени

            # if window_dict != words_dict:  через словарь не проходит/не принимает по времени
            if window_list_sort == words_list_sort:
                result += [start]

            start += 1
        return result



ex = Solution()

s= "ababaab"
words = ["ab","ba","ba"]
print(ex.findSubstring(s, words))


words = ["ab","ba","ba"]
s = "ababaab"
print(ex.findSubstring(s, words))

words = ["a","a"]
s = "aaa"
print(ex.findSubstring(s, words))