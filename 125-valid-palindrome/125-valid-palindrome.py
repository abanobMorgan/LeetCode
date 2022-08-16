import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=re.sub(r'[\W_]+', '', s)
        s = s.lower()
        if s == s[::-1]: 
            return True 
        return False 