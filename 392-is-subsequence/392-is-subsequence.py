class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #s of t
        
        new_str=""
        if len(s)==0:
            return True
        n,m=len(s),len(t)
        i,j=0,0
        
        while (i<n and j<m):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==n