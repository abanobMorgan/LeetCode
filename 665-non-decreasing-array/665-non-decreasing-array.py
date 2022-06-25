class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        validation_check=False        
        for i in range(1, len(nums)):                       
            if nums[i]<nums[i-1]:
                if validation_check:
                    return False
                validation_check = True
                print(validation_check)
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]                       
        return True