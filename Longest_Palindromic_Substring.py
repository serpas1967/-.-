class Solution:
    def longestPalindrome(self, s: str) -> str:
        index = 0
        palindroms = [s[0]]
        longest = True
        while index < len(s):
            back = len(s)
            while longest and back > 1:
                if s[index: back] == s[index: back][::-1]:
                    if len(palindroms[-1]) < len(s[index: back]):
                        palindroms.append(s[index: back])
                    break
                back -= 1    
            index += 1

        return palindroms[-1]  