class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ''
        ind = 0
        flag = True
        while flag:
            prefix += strs[0][ind]
            for word in strs:
                if prefix not in word[:ind + 1]:
                    flag = False
                    prefix = prefix[:-1]
                    break

            ind += 1
        return prefix


data = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(data))

data = ["dog", "racecar", "car"]
print(Solution().longestCommonPrefix(data))
