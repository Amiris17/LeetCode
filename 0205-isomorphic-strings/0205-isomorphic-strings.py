class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def helper(word):
            output,lookup=[],{}
            i=1
            for w in word:
                if w not in lookup:
                    lookup[w]=i
                    i+=1
                output.append(lookup[w])
            return output
        return helper(s)==helper(t)
    
    
    #followed yhoutube guide but bascially this prtoblems is kinda confusing but think of the letters as numbersa nd then see if the numbers will match on borh sides
    
    #differnt to dictionary because tahts accounting FOR EACH letter as 1 or more but never as in order etc
    
    
    #abbc A=1 B=2 B=2 C=3 in comparison to dictionary itd be liek 1 2,1 which doesnt help for fair comparison
    #wed have to loop through both dictionaries and compare simulatenously
    
    