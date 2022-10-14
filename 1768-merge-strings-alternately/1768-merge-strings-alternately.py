class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
       
        result=""
        
        #step lets make both strings of equal length
        
        
        #chck equal lengths first
        if len(word1)==len(word2):
            for i in range(len(word1)):
                result+=word1[i]
                result+=word2[i]
            return result
        
        if len(word1)>len(word2):
           
            for i in range(len(word2)):
                result+=word1[i]
                result+=word2[i]
            result+=word1[i+1:]
            
            return result
            
        if len(word2)>len(word1):
             #saving index redmmeber because were spliciing 
            for i in range(len(word1)):
                result+=word1[i]
                result+=word2[i]
            
            
            return result+word2[i+1:]