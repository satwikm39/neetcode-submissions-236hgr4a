class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            if s[r] not in unique:
                unique.add(s[r])
                res = max(r - l + 1, res)
        return res

