class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            q = collections.deque()
            q.append((i,j))
            visit.add((i,j))
            
            while q:
                row, col = q.popleft()
                dirctions = [(0,1),(0,-1),(-1,0),(1,0)]
                for dr, dc in dirctions:
                    r, c = row + dr, col + dc
                    if ((r >= 0 ) and c >=0 and
                        ( r<len(grid)) and 
                        (c < len(grid[0])) and 
                        (grid[r][c] == "1") and 
                        ((r,c) not in visit)):
                        
                        q.append((r,c))
                        visit.add((r,c))
        
        
        
        islands = 0
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    islands += 1
                    
        return islands