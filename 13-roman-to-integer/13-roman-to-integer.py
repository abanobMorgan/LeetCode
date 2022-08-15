class Solution:
    def romanToInt(self, s: str) -> int:
        
        # rti is a dict for roman to intgers values
        romandict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        # ans is for our sum value
        ans=0

        # for loop till len(s)-1 cause last Roman Value cant compare
        for a in range(len(s)-1):
            if romandict[s[a]] < romandict[s[a+1]]:
                ans = ans - romandict[s[a]]
            else:   
                ans = ans + romandict[s[a]]

        # So we add it and return the final ans
        return ans+ romandict[s[-1]]