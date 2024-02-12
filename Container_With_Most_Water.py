class Solution:
    def maxArea(self, height: list[int]) -> int:
        """ вначале(закомментированное) использовал проход по всем возможным комбинациям,
         НО нарушал ограничения по ВРЕМЕНИ !!!
         решил двигаться с противоположных концов списка, ВЫБИРАЯ предположительно БОЛЬШУЮ(следующую)
        высоту(значение),  точнее, ТОЧНО оставляя позади меньшую из высот,
        тк если текущее значение этой лимитирующей высоты при умножении на текущее(макс.) расстояние
        (высота * длина) не улучшает square, то дальнейшие варианты с этой высотой уже точно не будут лучше,
         тк второй множитель(длина) будет только уменьшаться"""

        square = min(height[0], height[-1]) * (len(height) - 1)
        i = 0
        j = len(height) - 1
        while i != j:
        #for i in range(len(height) - 1):
        #    for j in range(len(height) - 1, i, -1):
                if square >= min(height[i], height[j]) * (j - i):
                    if height[i] < height[j]:
                        i += 1
                    else:
                        j -= 1
                square = max(square, min(height[i], height[j]) * (j - i))
        return square

height = [1,8,6,2,5,4,8,3,7]
height = [2,3,4,5,18,17,6]
ex = Solution()
print(ex.maxArea(height))