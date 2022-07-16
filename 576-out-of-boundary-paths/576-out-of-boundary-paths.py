class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9+7
        get_neighbors = lambda r, c: [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        add = lambda n1, n2: ((n1 % mod) + (n2 % mod)) % mod
        is_inbound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        # Think about 3D matrix as K matrixes stacked on top of each other with m*n dimensions
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove + 1)]
        
        # DP Transition
        for k in range(1, maxMove + 1):
            for row in range(m):
                for col in range(n):
                    for next_row, next_col in get_neighbors(row, col):
                        if not is_inbound(next_row, next_col):
                            dp[k][row][col] = add(dp[k][row][col], 1)
                        else:
                            dp[k][row][col] = add(dp[k][row][col], dp[k-1][next_row][next_col]) 
                  
        return dp[maxMove][startRow][startColumn]