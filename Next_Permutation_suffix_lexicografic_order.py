class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        turn = 0
        suf = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                turn = i - 1  # точка поворота(непосредственно перед суффиксом)
                suf = i  # начало наибольшего НЕувеличивающегося суффикса
                break

        if suf == 0:
            return sorted(nums)

        for j in range(len(nums) - 1, suf - 1, -1):
            if nums[j] > nums[turn]:
                nums[j], nums[turn] = nums[turn], nums[j]
                break

        nums = nums[:turn + 1] + sorted(nums[suf:])
        return nums


ex = Solution()
case = [1,2,3]
print(ex.nextPermutation(case))

case = [3,2,1]
print(ex.nextPermutation(case))

case = [1,1,5]
print(ex.nextPermutation(case))