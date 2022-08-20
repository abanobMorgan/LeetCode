from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squs = defaultdict(set) # keys here must be r/3 and c/3 
        
        
        for r in range(len(board)): 
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squs[(r//3, c//3)]):
                        return False 
                    
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squs[(r//3, c//3)].add(board[r][c])
                
        return True 
        