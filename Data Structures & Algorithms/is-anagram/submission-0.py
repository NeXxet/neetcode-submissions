class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        for c in s: 
            map[c] += 1

        for c in t:
            map[c] -= 1

        for value in map.values():
            if value != 0:
                return False

        return True