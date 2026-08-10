class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()

        left = right = result = 0

        while right < len(s):
            if s[right] not in uniques:
                uniques.add(s[right])
                right += 1
            else:
                uniques.remove(s[left])
                left += 1
            result = max(result, right-left)
        return result