class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for ind, num in enumerate(numbers):
            if target - num in numbers[ind + 1:]:
                return [ind + 1, numbers.index(target - num, ind + 1) + 1]

numbers = [2,7,11,15]
target = 9
example = Solution()
print(example.twoSum(numbers, target))

numbers = [-1,0]
numbers = [-1,-1,1,1] #,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = -2
print(example.twoSum(numbers, target))

numbers = [2,3,4]
target = 6
print(example.twoSum(numbers, target))