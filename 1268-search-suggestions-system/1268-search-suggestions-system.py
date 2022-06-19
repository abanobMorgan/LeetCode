class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.suggestions = list()
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        
        # sort the input lexicographically
        # before inserting them into the trie
        products.sort()
        
        # now, the usual trie insertion
        # pattern but for every word given to us
        for product in products:
            cur = root
            for letter in product:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            
                # once we've moved to the first letter
                # of the current word, add the current
                # word to it's suggestion list (at most 3)
                # and this list will be sorted since we've
                # done the sorting beforehand
                # now, for every letter for every word in the trie
                # it'll have an additional list with the 3 most
                # close suggestions
                if len(cur.suggestions) < 3:
                    cur.suggestions.append(product)
            
            cur.end = True
            
        # init the result object, the judge
        # needs this pattern if there are
        # no valid answers
        res = [[]] * len(searchWord)
        
        cur = root
        
        # iterate over all the letters
        # in the given searchWord and
        # gather the suggestions
        for i in range(len(searchWord)):
            if searchWord[i] not in cur.children:
                break
            
            # we're moving to the node before
            # getting the suggestions because
            # in the first iteration, this will
            # be the root node (we followed a similar
            # pattern while populating the trie too)
            cur = cur.children[searchWord[i]]
            res[i] = cur.suggestions
        
        return res