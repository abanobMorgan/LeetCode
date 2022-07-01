class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        
        totalUnits = 0
        for numberOfBoxes, numberOfUnitsPerBoxi in boxTypes:
            # Take as many boxes until we're out of space on the truck
            # or we're out of boxes of this type
            numBoxes = min(truckSize, numberOfBoxes)
            
            totalUnits += numBoxes * numberOfUnitsPerBoxi
            truckSize -= numBoxes
        return totalUnits