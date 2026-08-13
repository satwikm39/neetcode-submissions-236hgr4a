from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq1, freq2 = defaultdict(int), defaultdict(int)

        for n in s:
            freq1[n] += 1
        for n in t:
            freq2[n] += 1
        
        if freq1 == freq2:
            return True
        else:
            return False
