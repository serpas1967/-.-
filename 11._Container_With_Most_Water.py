class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_vol = 0
        start = 0
        dimension = len(height)
        end = dimension - 1
        while start != end:
            current_vol = min(height[start], height[end] ) * (end - start)
            if current_vol > max_vol:
                max_vol = current_vol
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
            
        return max_vol