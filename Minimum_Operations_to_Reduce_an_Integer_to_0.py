class Solution:
    def minOperations(self, n: int) -> int:
        """ Идея состоит в том, чтобы находить ближайшее к числу N число х = 2 ** degree,
            затем , вычислив модуль разницы между  N и x и присвоив N = N - x  либо N = x - N(
            чтобы N оказалось положительным,т.е. модуль!!! ),
            опять найти ближайшее к числу N число х = 2 ** degree
            и так повторять , пока N не станет равным нулю. 
            Количество (meter) этих шагов/операций и есть минимальное количество операций сложения 
            или вычитания
        :param n: 
        :return: 
        """
        meter = 0
        if n == 1 or n == 2:
            return 1
        while n != 0:
            degree = 0
            x = 0
            while (n - x) > 0 :
                x = 2 ** degree
                degree += 1
            if n - x // 2 <= x - n:
                n = n - x // 2
            else:
                n = x - n
            meter += 1
        return meter

print(Solution().minOperations(39))
print(Solution().minOperations(54))
print(Solution().minOperations(761))
