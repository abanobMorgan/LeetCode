class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        ans = log(n, 4)
        return ans - trunc(ans) == 0
