class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #IDEA make a hash table and just add whatever isnt in the hash_table from string since t_length>s_length
        
        #t always bigger than s.
        
        
        d={}
        d1={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i in range(len(t)):
            if t[i] in d1:
                d1[t[i]]+=1
            else:
                d1[t[i]]=1
        
        
            
        value=set(d.items())
        value2=set(d1.items())
        
        fin=dict(value2-value)
        
        for x in fin:
            return x
        
        
       
        
            
            
            
        