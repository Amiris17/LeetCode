class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)==0:
            return False
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #new approach make two lists and just compare
        MAPST={}
        MAPTS={}
        for i in range(len(s)):
            p1,p2=s[i],t[i]
            
            if p1 in MAPST and MAPST[p1] != p2 or p2 in MAPTS and MAPTS[p2]!=p1:
                return False
            
            
            
            
            MAPST[p1]=p2
            MAPTS[p2]=p1
            
                       
           
        return True
            
        
      
     

            
            
        