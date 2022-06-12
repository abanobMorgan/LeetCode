class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = 0 
        j = 0 
        n = len(nums)
        numMap = {}        
        max_unique_sum = 0 
        current_sum = 0
        while j < n:
            numMap[nums[j]] = numMap.get(nums[j], 0) + 1
            current_sum += nums[j]
            while i < j and numMap[nums[j]] > 1:
                numMap[nums[i]] -= 1
                current_sum -= nums[i]
                i += 1
                        
            max_unique_sum = max(max_unique_sum, current_sum)
            j+=1
        
        return max_unique_sum