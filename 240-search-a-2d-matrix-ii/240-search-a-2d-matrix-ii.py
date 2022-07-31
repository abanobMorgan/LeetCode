class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows,cols = len(matrix),len(matrix[0])
        for i in range(rows):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                col_no = bisect_left(matrix[i],target)
                if matrix[i][col_no] == target: return True
            elif matrix[i][0]>target: break
        return False