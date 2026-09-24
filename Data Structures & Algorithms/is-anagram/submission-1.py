class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Num. of char in both strings 
        countS, countT = {} , {}

        for i in range(len(s)):
            # Count occurence of each character in the string
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # compares the number of occurences for s and t    
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True    

        