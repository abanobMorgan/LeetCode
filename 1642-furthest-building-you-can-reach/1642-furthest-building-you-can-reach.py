class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        largestJumps = []
        remainingJumps = 0
        
        for idx in range(1, len(heights)):
            height = heights[idx] - heights[idx-1]
            if height > 0:
                heapq.heappush(largestJumps, height)
            if len(largestJumps) > ladders:
                remainingJumps += heapq.heappop(largestJumps)
            if remainingJumps > bricks:
                return idx-1
            
        return idx