class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Map = defaultdict(int)
        windowMap = defaultdict(int)

        windowStart = 0
        windowEnd = len(s1)-1

        for c in s1:
            s1Map[c] += 1
        
        for i in range(len(s1)):
            windowMap[s2[i]] += 1

        while windowEnd < len(s2):
            if s1Map == windowMap:
                return True
            
            windowMap[s2[windowStart]] -= 1
            if windowMap[s2[windowStart]] == 0:
                del windowMap[s2[windowStart]]
            windowStart += 1

            if windowEnd + 1 < len(s2):
                windowEnd += 1
                windowMap[s2[windowEnd]] += 1
            else:
                windowEnd += 1

        return False
