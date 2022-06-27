class Solution:
    def minPartitions(self, n: str) -> int:
        x =  [int(char) for char in n]
        return max(x)