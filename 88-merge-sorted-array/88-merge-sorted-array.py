class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m+n-1):
            for j in range(n):
                if nums1[i] >= nums2[j] :  
                    nums1.insert(i,nums2[j])
                    nums2.pop(j)
                    nums1.pop(-1)
                    n-=1
                    print(nums1, i, nums2)
                    break
        for i in range(1,n+1): 
            nums1[-i] = nums2[-i]