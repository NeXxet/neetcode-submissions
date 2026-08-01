from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        if window_size > len(s2):
            return False
        
        target = Counter(s1)
        window_map = Counter(s2[:len(s1)])

        if window_map == target:
            return True

        for right in range(window_size, len(s2)):
            left = right - window_size
            
            window_map[s2[left]] -= 1
            if window_map[s2[left]] == 0:
                del window_map[s2[left]]

            window_map[s2[right]] += 1

            if window_map == target:
                return True

        return False
