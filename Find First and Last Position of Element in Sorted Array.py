class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        numbers = [i for i in range(len(nums)) if nums[i] == target]
        if len(numbers) == 0:
            return result
        elif len(numbers) == 1:
            return [numbers[0], numbers[0]]
        else:
            return [numbers[0], numbers[-1]]