class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        pre_sum={-1:0}
        ssum=sum(nums)
        n=len(nums)
        if n==1:
            return 1 if nums[0]==x else -1
        
        for i,val in enumerate(nums):
            pre_sum[i]=pre_sum[i-1]+val
        i,j=0,0
        ans=sys.maxsize
        
        while i<n and j<n:
            while j<n and (pre_sum[j]-pre_sum[i-1])<ssum-x:
                j+=1
            if j<n and (pre_sum[j]-pre_sum[i-1])==ssum-x:
                ans=min(ans,n-(j-i+1))
            i+=1
        return ans if ans!=sys.maxsize else -1       