class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
       
        result = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1): 
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    third =nums[nums.index(-(nums[i] + nums[j]))]
                    #if nums.index(-(nums[i] + nums[j])) != i and nums.index(-(nums[i] + nums[j])) != j:
                    #el1 = min(nums[i], nums[j], third)
                    #el3 = max(nums[i], nums[j], third)
                    #f = lambda x: sorted(x)
                    res = tuple(sorted([nums[i], nums[j], third]))
                    print(res)
                    result.add(res)
        return result

ex = Solution()
nums = [-1,0,1,2,-1,-4]
print(ex.threeSum(nums))