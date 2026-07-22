class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        maxVolume = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            volume = width * height

            maxVolume = max(maxVolume, volume)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxVolume