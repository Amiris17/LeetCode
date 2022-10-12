class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d1={}
        d2={}
        count=0 #if its 
        for i in s1:
            if i in d1: #If weve seen it before increase count
                d1[i]+=1
            else:          #if weve never seen count=1 repeat get counht for both strings gg    
                d1[i]=1
        for j in s2:
            if j in d2:
                d2[j]+=1
            else:
                d2[j]=1
            
        if d1==d2:
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count+=1
            return count ==2 or count==0
                
            
                
                
            
            
        
        
       
        
        
            
            
            
                
                    
        # we have twqo strings here and we just look for a character that they share swap them, then return s1==s2