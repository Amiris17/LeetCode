class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        
        if len (s) ==0 or len(t)==0:
            return False
        

        dict1={}
        dict2={}
        
        for i in s:
            if i in dict1: #If weve seen it before increase count
                dict1[i]+=1
            else:          #if weve never seen count=1 repeat get counht for both strings gg    
                dict1[i]=1
                
                
        for j in t:
            if j in dict2:
                dict2[j]+=1
            else:
                dict2[j]=1
            
        return dict1==dict2
        
       