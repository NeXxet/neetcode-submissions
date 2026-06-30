class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        viableRate = 0


        while low <= high:
            currentHours = 0
            mid = (low + high) // 2
            for pile in piles:
                currentHours += math.ceil(pile/mid)
            
            if currentHours <= h:
                viableRate = mid
                high = mid -1
            else:
                low = mid + 1
        
        return viableRate