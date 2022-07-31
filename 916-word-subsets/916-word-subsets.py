class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        result = []
        tempDict = Counter()
        for w in words2:
            tempDict |= Counter(w)
            
        
        for w in words1:
            if not tempDict - Counter(w):
                result.append(w)
                
        return result