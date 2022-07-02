class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort(reverse=True)
        verticalCuts.sort(reverse=True)
        hcMaxDiff = max(h - horizontalCuts[0], horizontalCuts[-1])
        vcMaxDiff = max(w - verticalCuts[0], verticalCuts[-1])
        
        for i in range(len(horizontalCuts)-1):
            diff = horizontalCuts[i] - horizontalCuts[i+1]
            if (diff > hcMaxDiff) :
                hcMaxDiff = diff
            
        for i in range(len(verticalCuts)-1):
            diff = verticalCuts[i] - verticalCuts[i+1]
            if diff > vcMaxDiff:
                vcMaxDiff = diff
            
        return (vcMaxDiff * hcMaxDiff) % 1000000007