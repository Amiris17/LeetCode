class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #s of t
        #TLDR Basically attempt1: we tried to manipulate the string however order came into play and stumped it so we instead  looped through using a WHILE LOOP because it gives us control over how we increment as opposed to a for loop. this allows us to check everything in string T with the current character string s and if we find a match increment s's index by one. 
        
        
        #new_str=""
        if len(s)==0:
            return True
        len1,len2=len(s),len(t)
        i,j=0,0
        
        while (i<len1 and j<len2):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len1