class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        meter = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[meter] = nums[i+1]
            else:
                if nums[:len(nums[:meter+1])].count(nums[i]) < 2:    
                    nums[meter] = nums[i]
                    #meter += 1                
            meter += 1                
        return meter 