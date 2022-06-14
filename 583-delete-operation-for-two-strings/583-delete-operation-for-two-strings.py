class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        
        M, N = len(word1), len(word2)
        dp = [j for j in range(N+1)]
        
        for i in range(1, M+1):
            new_dp = []
            for j in range(N+1):
                if j == 0:
                    elem = i
                elif word1[i-1] != word2[j-1]:
                    elem = 1 + min(dp[j], new_dp[j-1])
                else:
                    elem = min(1 + min(dp[j], new_dp[j-1]), dp[j-1])
                
                new_dp.append(elem)

            dp = new_dp
         
        return dp[-1]