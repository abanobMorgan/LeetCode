class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet=[".-","-...","-.-.","-..",".","..-.",
                  "--.","....","..",".---","-.-",".-..",
                  "--","-.","---",".--.","--.-",".-.",
                  "...","-","..-","...-",".--",

                  "-..-","-.--","--.."]
        seen = {"".join(alphabet[ord(c) - ord('a')] for c in word)
                for word in words}
        return len(seen)