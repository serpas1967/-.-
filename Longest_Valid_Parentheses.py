class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = []  #список помещаемых индексов для '('  и ')'
        distance_list = [0]  #список расстояний между корреспондирующися/соответствующими ( и )
        ind = 0 # индекс символов в строке s
        remember = - 1  # индекс последнего добавленного элемента '('
        while ind < len(s):
            if s[ind] == '(' and remember + distance_list[-1] == ind:  # начинаем считать
                result.append(remember)
            elif s[ind] == '(':
                result.append(ind)
            elif s[ind] == ')' and len(result) > 0: # если текущий элемент ) и
            # уже есть добавленный ранее (, то запоминаем в remember индекс того ранее добавленного (,
            #   удаляем его из result  и определяем  расстояние/длину от текущего )
            # до предыдущего/удаленного (
                remember = result.pop()
                distance = ind - remember + 1
                distance_list.append(distance)
            ind += 1
        return max(distance_list)


ex = Solution()
s = "((()))())"
print(ex.longestValidParentheses(s))