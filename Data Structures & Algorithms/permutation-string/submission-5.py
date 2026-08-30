from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_start = 0
        window_end = len(s1)-1
        
        s1Map = Counter(s1)
        window_map = Counter(s2[:len(s1)])

        while window_end < len(s2):
            if s1Map == window_map:
                return True
            
            window_map[s2[window_start]] -= 1
            if window_map[s2[window_start]] == 0:
                del window_map[s2[window_start]]
            window_start += 1

            if window_end + 1 < len(s2):
                window_end += 1
                window_map[s2[window_end]] += 1
            else:
                window_end += 1

        return False
