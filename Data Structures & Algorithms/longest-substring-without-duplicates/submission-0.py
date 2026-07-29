class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()

        left, result = 0, 0

        for right, c in enumerate(s):
            while c in uniques:
                uniques.remove(s[left])
                left += 1
            uniques.add(c)
            result = max(result, right-left+1)
        return result