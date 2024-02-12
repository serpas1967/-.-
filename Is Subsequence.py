class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind = 0

        for ch in s:
            if ch not in t[ind:] or ind > len(t):
                return False

            # ind = len(t[:ind]) + 1 + t[ind:].find(ch)
            #ind += (1 + t[ind:].find(ch))
            ind = t.find(ch, ind) + 1
        return True

s = "aaaaaa"
t = "bbaaaa"
example = Solution()
print(example. isSubsequence(s, t))

s = "abc"
t = "abhbgdc"
example = Solution()
print(example. isSubsequence(s, t))
print(t.find('b',2))